import unittest
from src.chat import *
from src.swen344_db_utils import connect

class TestChat(unittest.TestCase):

    #DB0 Unit Tests Rebuild/Drop

    def test_a_rebuild_tables(self):
        """Re-Build the tables"""
        conn = connect()
        cur = conn.cursor()
        rebuildTables()
        cur.execute('SELECT * FROM people')
        self.assertEqual([], cur.fetchall(), "no rows in people")
        conn.close()

    def test_a_rebuild_tables_is_idempotent(self):
        """Drop and rebuild the tables twice"""
        rebuildTables()
        rebuildTables()
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM people')
        self.assertEqual([], cur.fetchall(), "no rows in people")
        conn.close()

    #DB1 Unit Tests

    def test_b_populateTables(self):
        """Populate the tables and ensure that at least one of the tables was filled"""
        populateTables()
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT ID FROM people')
        self.assertEqual([(1,), (2,), (3,), (4,), (5,), (6,), (7,)], cur.fetchall(), "Missing IDs")
        conn.close()

    def test_cdb1_total_messages(self):
        """Checks count of total messages system wide"""
        conn = connect()
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(chatID) FROM messages """)
        results = cur.fetchall()
        countTotalM = [item[0] for item in results]
        self.assertEqual(14, countTotalM[0], "Total chat conversations incorrect")
        conn.close()

    def test_cdb1_unread_to_Moe(self):
        """Checks if amount of unread messages to Moe are correct"""
        conn = connect()
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(messages) FROM messages WHERE messages.receiver = 'Moe' AND messages.status = 'Unread' """)
        results = cur.fetchall()
        countAUnread = [item[0] for item in results]
        self.assertEqual(1, countAUnread[0], "Unread to Moe incorrect")
        conn.close()    

    def test_cdb1_unread_to_Abbott(self):
        """Checks if amount of unread messages to Abbott are correct"""
        conn = connect()
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(messages) FROM messages WHERE messages.receiver = 'Abbott' AND messages.status = 'Unread' """)
        results = cur.fetchall()
        countAUnread = [item[0] for item in results]
        self.assertEqual(3, countAUnread[0], "Unread to Abbott incorrect")
        conn.close()


    def test_cdb1_messages_Abbott_Costello(self):
        """Makes sure we can get all messages between Abbott and Costello"""
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(messages.chatID) FROM messages WHERE messages.chatID = 1 ')
        results = cur.fetchall()
        countAandCTotal = [item[0] for item in results]
        self.assertEqual(6, countAandCTotal[0], "Incorrect number of messages between Abbott and Costello")
        conn.close()

    def test_cdb1_messages_Moe_Larry_1995(self):
        """Makes sure we can get all messages between Moe and Larry during the year 1995"""
        conn = connect()
        cur = conn.cursor()
        #Doesnt track 1995 yet, but will shortly
        cur.execute('SELECT COUNT(messages.chatID) FROM messages WHERE messages.chatID = 2 ')
        results = cur.fetchall()
        countMandLTotal = [item[0] for item in results]
        self.assertEqual(5, countMandLTotal[0], "Incorrect number of messages between Abbott and Costello")
        conn.close()

    def test_cdb1_larry_suspension(self):
        """Check if Larry is suspended May 4, 2012"""
        conn = connect()
        cur = conn.cursor()

        cur.execute('SELECT startYear FROM suspension WHERE userID = 4 ')
        results = cur.fetchall()
        st = [item[0] for item in results]
        cur.execute('SELECT endYear FROM suspension WHERE userID = 4 ')
        results2 = cur.fetchall()
        end = [item[0] for item in results2]

        testResult = 0
        if(2012 > int(st[0]) and 2012 < int(end[0])):
            testResult = 1

        self.assertEqual(1, testResult, "Can't find suspension for Larry on May 4, 2012")

        conn.close()

    def test_cdb1_curly_suspension(self):
        """Check if Curly is not suspended February 29th, 2000"""
        conn = connect()
        cur = conn.cursor()

        cur.execute('SELECT endYear FROM suspension WHERE userID = 5 ')
        results = cur.fetchall()
        st = [item[0] for item in results]

        testResult = 0
        if(2000 > int(st[0])):
            testResult = 1

        self.assertEqual(1, testResult, "Suspension found for Curly on February 29th, 2000")

        conn.close()




    #DB2 UNIT TESTS

    #Flow of Messages

    def test_dadb2_create_user_bob(self):
        conn = connect()
        cur = conn.cursor()
        
        #Calling him BOBbyBoy34 instead of Bob to comply with 8 character minimum for new usernames
        create_user('8', 'BOBbyBoy34', 'BobbyBoy34@gmail.com', '012-522-5544', '742-123-1234')

        cur.execute("""SELECT COUNT(*) FROM people""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual(8, st[0], "Incorrect Number of People within Database:  Bob was not created")

        conn.commit()
        conn.close()

    def test_dbdb2_send_message_BobToMarv(self):
        conn = connect()
        cur = conn.cursor()

        send_new_message('Im doing work, Im baby-stepping', 'DrMarvin', 'BOBbyBoy34', '05-18-1991')

        cur.execute("""SELECT messages.sender FROM messages WHERE messages.message = 'Im doing work, Im baby-stepping'""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual('BOBbyBoy34', st[0], "Incorrect Number of People within Database:  Bob was not created")

        conn.close()
    
    def test_dcdb2_username_change_Bob(self):
        conn = connect()
        cur = conn.cursor()

        update_username('BOBbyBoy34', 'BabySteps2Door', '05-19-1991')

        cur.execute("""SELECT people.username FROM people WHERE people.ID = '8'""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual('BabySteps2Door', st[0], "Bob was unable to change his username")

        conn.close()

    def test_dddb2_username_change_within_six_months_Bob(self):
        with self.assertRaises(Exception) as context:
            update_username('BabySteps2Door', 'BabySteps2Elevator', '05-19-1991')
        self.assertTrue('Username cannot be changed more than once in 6 months' in str(context.exception))

    def test_dedb2_check_message_DrMarvin(self):
        self.assertEqual(['BabySteps2Door'], check_messages('DrMarvin'), "DrMarvin doesn't have any messages from BabySteps2Door")

    def test_dfdb2_mark_message_as_read(self):
        conn = connect()
        cur = conn.cursor()

        cur.execute("""SELECT messages.status FROM messages WHERE messages.message = 'Im doing work, Im baby-stepping'""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual('Unread', st[0], "Message should be unread")

        mark_message_read('DrMarvin','Im doing work, Im baby-stepping','BabySteps2Door')

        cur.execute("""SELECT messages.status FROM messages WHERE messages.message = 'Im doing work, Im baby-stepping'""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual('Read', st[0], "Message should be read")

        conn.close()
    
    #Suspension

    def test_dgdb2_suspended_sender(self):
        with self.assertRaises(Exception) as context:
            send_new_message('Attention! This is Larry', 'Moe', 'Larry', '05-05-2012')
        self.assertTrue("""User is suspended from sending messages until '01-01-2060'""" in str(context.exception))

    def test_dhdb2_break_suspension(self):
        account_suspension('Clear', '4')
        send_new_message('Attention! This is Larry', 'Moe', 'Larry', '05-05-2012')
        
        conn = connect()
        cur = conn.cursor()

        cur.execute("""SELECT messages.date FROM messages WHERE messages.message = 'Attention! This is Larry'""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual('05-05-2012', st[0], "User not successfully cleared of suspension")

        conn.close()
    
    #CSV

    def test_didb2_read_csv_into_db(self):
        read_csv_into_db('whos_on_first.csv')

        conn = connect()
        cur = conn.cursor()

        cur.execute("""SELECT messages.status FROM messages WHERE messages.time = '00:00'""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual('Unread', st[0], "CSV not loaded correctly into database")

        conn.close()
        





    #DB3 Tests

    def test_eadb3_populated_tables(self):
        """Populate the tables and ensure that at least one of the tables was filled"""
        populate_community_tables()
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM community')
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual(2, st[0], "Missing Communities")
        conn.close()

    def test_ebdb3_create_user(self):
        #Using LexFromTex instead of Lex because of 8 character min on username creation
        conn = connect()
        cur = conn.cursor()
        
        create_user('9', 'LexFromTex', 'LexFromTex@hotmail.com', '045-125-1622', '845-023-1252')
        
        cur.execute("""SELECT COUNT(*) FROM people""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual(9, st[0], "Incorrect Number of People within Database:  LexFromTex was not created")

        #Lex and Moe have a quick conversation
        send_new_message('Hey Moe, Im new here', 'Moe', 'LexFromTex', '2-23-2021')
        send_new_message('Welcome to the community!', 'LexFromTex', 'Moe', '2-23-2021')
        send_new_message('Thanks! Glad to be here', 'Moe', 'LexFromTex', '2-23-2021')
        send_new_message('Let me know if you have any questions', 'LexFromTex', 'Moe', '2-23-2021')
        send_new_message('I will definitely reach out', 'Moe', 'LexFromTex', '2-23-2021')


        conn.close()

    def test_ecdb3_join_community(self):
        conn = connect()
        cur = conn.cursor()

        community_membership('Join', 'LexFromTex', 'Metropolis')

        cur.execute("""SELECT community.community_members FROM community WHERE community.community_name = 'Metropolis'""")
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_members = st[0].split(',')
        joined = 0
        if('LexFromTex' in curr_members):
            joined = 1
        self.assertEqual(1, joined, "LexFromTex was not able to join Metropolis")

        conn.close()
    
    def test_eddb3_chan_message(self):
        send_community_message('LexFromTex', 'Metropolis', '#DailyPlanet', 'Whats going on in the planet today?')
        clarksunreadmetro = get_count_unread_community('Community', 'clarknotsuperman', 'Metropolis')
        self.assertEqual(1, clarksunreadmetro, "LexFromTex was not able to send a message in Metropolis")

    def test_eedb3_mention(self):
        send_community_message('LexFromTex', 'Metropolis', '#DailyPlanet', '@clarknotsuperman are you the only one here?')
        clarksmentions = get_mentions('clarknotsuperman')
        self.assertEqual(['@clarknotsuperman are you the only one here?'], clarksmentions, "Mentions not working")

    def test_efdb3_mention_not_in_community(self):
        send_community_message('Moe', 'Comedy', '#Dialogs', '@clarknotsuperman you wish you were funny LOL')
        clarksmentions = get_mentions('clarknotsuperman')
        self.assertEqual(['@clarknotsuperman are you the only one here?'], clarksmentions, "Mentions should not include members not in communities")

    def test_egdb3_sus_and_send(self):
        suspend_community('Suspend', 'LexFromTex', 'Metropolis')
        with self.assertRaises(Exception) as context:
            send_community_message('LexFromTex', 'Metropolis', '#DailyPlanet', 'This planet blows, Im moving to Mars!')
        self.assertTrue("""User is a suspended member of this channel""" in str(context.exception))

        community_membership('Join', 'LexFromTex', 'Comedy')
        send_community_message('LexFromTex', 'Comedy', '#Dialogs', 'I got suspended from Metropolis and I think its cuz clark likes being alone')
        
        conn = connect()
        cur = conn.cursor()

        cur.execute("""SELECT sender FROM community_channels WHERE chan_message = '%s'""" % ('I got suspended from Metropolis and I think its cuz clark likes being alone'))
        results = cur.fetchall()
        st = [item[0] for item in results]
        self.assertEqual('LexFromTex', st[0], 'Message was not sent in either channel')

        conn.close()




    #Db4 Tests

    def test_fadb4_get_communities(self):
        com = 'Comedy'
        st = get_channels_community(com)
        self.assertEqual(['#ArgumentClinic', '#Dialogs'], st, 'Incorrect channels within Comedy community')
    
    def test_fbdb4_get_communities(self):
        coms = get_communities()
        self.assertEqual(['Metropolis', 'Comedy'], coms, 'Could not get communities')

    def test_fcdb4_check_date_range(self):
        mess_date = '2-25-2021'
        s_date = '2-01-2021'
        e_date = '3-01-2021'
        result = check_date_inbetween(mess_date, s_date, e_date)
        self.assertEqual(1, result, 'Date was not between given set')

    def test_fddb4_search_reply(self):
        result = search_community_message('Comedy', 'reply')
        self.assertEqual(['reply please', 'I replied already!'], result, 'Incorrect result for search of reply string')

    def test_fedb4_search_reply_please(self):
        result = search_community_message('Comedy', 'reply please')
        self.assertEqual(['reply please'], result, 'Incorrect result for search of reply please string')

    def test_ffdb4_moderator_query(self):
        #Checks moderator query function (my understanding)
        result = moderator_query('2-28-2021')
        self.assertEqual(['LexFromTex'], result, 'Lex not found in results')

        #Checks suspended users in a community
        result = get_user_suspended('Metropolis')
        self.assertEqual(['LexFromTex'], result, 'Lex not found in results')

    def test_fgdb4_activity_summary(self):
        result = activity_summary('3-3-2021')
        self.assertEqual([('Metropolis', '0.067', '1'),('Comedy', '0.2', '4')], result, 'Activity Summary not correct')

