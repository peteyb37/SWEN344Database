from src.swen344_db_utils import connect
from datetime import datetime, timedelta
from csv import reader

def rebuildTables():
    """
    Drops and Rebuilds the tables
    Args: 
        None
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()
    drop_sql = """
        DROP TABLE IF EXISTS people;
        DROP TABLE IF EXISTS conversation;
        DROP TABLE IF EXISTS messages;
        DROP TABLE IF EXISTS suspension;
        DROP TABLE IF EXISTS community;
        DROP TABLE IF EXISTS community_channels
    """
    people_sql = """
        CREATE TABLE people(
            ID int,
            username varchar(255),
            email varchar(255),
            ssn varchar(255),
            phone varchar(255),
            username_change varchar(255)
        )
    """
    conversation_table = """
        CREATE TABLE conversation(
            chatID int,
            user1 varchar(255),
            user2 varchar(255),
            totalMessages int
        )
    """
    messages_table = """
        CREATE TABLE messages(
            chatID int,
            message varchar(255),
            time varchar(255),
            date varchar(255),
            status varchar(255),
            sender varchar(255),
            receiver varchar(255)
        )
    """
    suspension_table = """    
        CREATE TABLE suspension(
            userID int,
            start varchar(255),
            expiration varchar(255),
            startYear varchar(255),
            endYear varchar(255)
        )
    """
    community_table = """
        CREATE TABLE community(
            community_name varchar(255),
            community_members varchar(1000),
            community_suspended_users varchar(1000),
            community_channels varchar(1000)
        )
    """
    community_channels_table = """
        CREATE TABLE community_channels(
            channel_name varchar(255),
            community_name varchar(255),
            sender varchar(255),
            time varchar(255),
            date varchar(255),
            chan_message varchar(255),
            status varchar(255)
        )
    """

    cur.execute(drop_sql)
    cur.execute(people_sql)
    cur.execute(conversation_table)
    cur.execute(messages_table)
    cur.execute(suspension_table)
    cur.execute(community_table)
    cur.execute(community_channels_table)
    conn.commit()
    conn.close()

def populateTables():
    """
    Populates the tables with starting data
    Args: 
        None
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    """People table"""
    cur.execute("INSERT INTO people (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('1', 'Abbott', 'AllAbbottMe@gmail.com', '734-11-4827', '716-034-8172', '00-00-0000'))
    cur.execute("INSERT INTO people (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('2', 'Costello', 'WheresElvis@gmail.com', '873-13-1523', '716-038-4817', '00-00-0000'))
    cur.execute("INSERT INTO people (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('3', 'Moe', 'MoeFromMoes@gmail.com', '836-91-2233', '845-519-2836', '00-00-0000'))
    cur.execute("INSERT INTO people (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('4', 'Larry', 'LarryBirddd@gmail.com', '777-87-3737', '585-283-1827', '00-00-0000'))
    cur.execute("INSERT INTO people (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('5', 'Curly', 'CurlyHair87@gmail.com', '434-81-2937', '803-174-1199', '00-00-0000'))
    cur.execute("INSERT INTO people (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('6', 'DrMarvin', 'DocMarv@gmail.com', '712-83-3427', '682-333-1157', '00-00-0000'))
    cur.execute("INSERT INTO people (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", ('7', 'clarknotsuperman', 'clarkKent007@gmail.com', '999-73-3311', '646-552-1411', '00-00-0000'))



    """Messages Table"""

    """Abbott to Costello"""
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'Hey man, how are you', '19:00', '06-23-1922', 'Read', 'Abbott', 'Costello'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'Im good bro but Ive been off site for a bit, sorry for the late response', '11:00','06-24-1923', 'Read', 'Costello', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'All good, Ive  been quite busy myself', '19:00', '12-01-1934', 'Unread', 'Abbott', 'Costello'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'Do you still have my jersey', '11:32', '02-19-1945', 'Read', 'Abbott', 'Costello'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'No... theres a war going on, I dont  have time for this', '16:34', '02-19-1945', 'Read', 'Costello', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('1', 'Sorry bro', '13:43', '03-01-1945', 'Unread', 'Abbott', 'Costello'))

    """Abbott to Moe"""
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('3', 'Check out my new hit single on Spotify', '12:00', '06-23-1937', 'Unread', 'Moe', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('3', 'Come on please dude pick up', '15:32', '06-01-1938', 'Unread', 'Moe', 'Abbott'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('3', 'Are you ignoring me?', '18:22', '09-03-1940', 'Unread', 'Moe', 'Abbott'))



    """Moe to Larry"""
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'You going to the bar tn', '15:00', '05-19-1995', 'Read', 'Moe', 'Larry'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'Yeah dude... better see you there', '15:34', '05-19-1995', 'Read', 'Larry', 'Moe'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'bruhhhh whera ae you i ned a riyde home', '00:23', '05-20-1995', 'Read', 'Moe', 'Larry'))
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'Sorry dude, Lindsey felt sick so we went back to her place', '00:45', '05-20-1995', 'Unread', 'Larry', 'Moe'))    
    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('2', 'I lost my phone that one night we went to the bar, sorry if you were worried', '14:00', '06-28-1995', 'Unread', 'Moe', 'Larry'))


    """Conversation Table"""
    cur.execute('SELECT COUNT(messages.chatID) FROM messages WHERE messages.chatID = 1 ')
    results = cur.fetchall()
    countAandC = [item[0] for item in results]
    cur.execute("INSERT INTO conversation (chatID, user1, user2, totalMessages) VALUES (%s, %s, %s, %s);", ('1', 'Abbott', 'Costello', countAandC[0]))
 
    cur.execute('SELECT COUNT(messages.chatID) FROM messages WHERE messages.chatID = 2 ')
    results = cur.fetchall()
    countMandL = [item[0] for item in results]
    cur.execute("INSERT INTO conversation (chatID, user1, user2, totalMessages) VALUES (%s, %s, %s, %s);", ('2', 'Moe', 'Larry', countMandL[0]))

    """Suspension Table"""
    cur.execute("INSERT INTO suspension (userID, start, expiration, startYear, endYear) VALUES (%s, %s, %s, %s, %s);", ('4', '01-01-2010', '01-01-2060', '2010', '2060'))
    cur.execute("INSERT INTO suspension (userID, start, expiration, startYear, endYear) VALUES (%s, %s, %s, %s, %s);", ('5', '01-01-1990', '12-31-1999', '1990', '1999'))

    conn.commit()
    conn.close()


def populate_community_tables():
    """
    Populates the community tables with starting data
    Args: 
        None
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    """Community Table"""
    cur.execute("INSERT INTO community (community_name, community_members, community_suspended_users, community_channels) VALUES (%s, %s, %s, %s);", ('Metropolis', 'clarknotsuperman', '', '#DailyPlanet,#Random'))
    cur.execute("INSERT INTO community (community_name, community_members, community_suspended_users, community_channels) VALUES (%s, %s, %s, %s);", ('Comedy', 'Abbott,Costello,Moe,Larry,Curly,DrMarvin,BabySteps2Door', '', '#ArgumentClinic,#Dialogs'))



    """Channels Table"""
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, chan_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogue', 'Comedy', 'Abbott', '5:16', '03-00-2021', 'reply please', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, chan_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogue', 'Comedy', 'Moe', '7:32', '03-00-2021', 'I replied already!', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, chan_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogue', 'Comedy', 'Costello', '9:22', '03-04-2020', 'say less my guy', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, chan_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogue', 'Comedy', 'Larry', '10:10', '03-00-2021', 'hey', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, chan_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogue', 'Comedy', 'Curly', '11:11', '03-00-2021', 'whats going on', 'Read'))
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, chan_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", ('#Dialogue', 'Comedy', 'Abbott', '14:14', '03-00-2021', 'ayyyyyyye', 'Read'))

    conn.commit()
    conn.close()

def check_date_inbetween(date_of_message, start_date, end_date):

    dateM = date_of_message.split('-')
    startSus = start_date.split('-')
    endSus = end_date.split('-')


    #Checks if date falls in between years :: Returns after all other statements
    if(int(dateM[2]) >= int(startSus[2]) and int(dateM[2]) <= int(endSus[2])):
        #If the year falls in between the years and is not equal to either
        if(int(dateM[2]) > int(startSus[2]) and int(dateM[2]) < int(endSus[2])):
            return 1
        #If the year is the same as the starting year and less than the end year
        elif(int(dateM[2]) == int(startSus[2]) and int(dateM[2]) < int(endSus[2])):
            #Is the month before the starting month?
            if(int(dateM[0]) < int(startSus[0])):
                return 0
            #Is the month after the starting month?
            elif(int(dateM[0]) > int(startSus[0])):
                return 1
            #Is the month the same?
            else:
                #Is the day before the starting day?
                if(int(dateM[1]) < int(startSus[1])):
                    return 0
                #Is the day after or equal to the starting day?
                else:
                    return 1
        #If the year is greater than the starting year and equal to the end year
        elif(int(dateM[2]) > int(startSus[2]) and int(dateM[2]) == int(endSus[2])):
            #Is the month after the end month?
            if(int(dateM[0]) > int(endSus[0])):
                return 0
            #Is the month before the end month?
            elif(int(dateM[0]) < int(endSus[0])):
                return 1
            #Is the month the same?
            else:
                #Is the day after the end day?
                if(int(dateM[1]) > int(endSus[1])):
                    return 0
                #Is the day before or equal to the end day?
                else:
                    return 1
        #If the year for all of the above is the same
        else:
            #Is the month before the start or after the end?
            if(int(dateM[0]) < int(startSus[0]) or int(dateM[0]) > int(endSus[0])):
                return 0
            #Is the month after the start and before the end?
            elif(int(dateM[0]) > int(startSus[0]) and int(dateM[0]) < int(endSus[0])):
                return 1
            #Is the month the same as the start and before the end?
            elif(int(dateM[0]) == int(startSus[0]) and int(dateM[0]) < int(endSus[0])):
                #If the day is the same or after the start day
                if(int(dateM[1]) >= int(startSus[1])):
                    return 1
            #Is the month after the start and the same as the end?
            elif(int(dateM[0]) > int(startSus[0]) and int(dateM[0]) == int(endSus[0])):
                #If the day is the same or before the end day
                if(int(dateM[1]) <= int(endSus[1])):
                    return 1
            #Is the month the same for all of the above?
            else:
                #Is the day before the start or after the end?
                if(int(dateM[1]) >= int(startSus[1]) and int(dateM[1]) <= int(endSus[1])):
                    return 1

    return 0


def getTimeAndDate():
    """
    Gets the current time and date and transforms it into the correct format
    Args: 
        None
    Returned:
        Current time and current date
    """
    dateTimeObj = datetime.now()
    time = str(dateTimeObj.hour) + ":" + str(dateTimeObj.minute)
    date = str(dateTimeObj.month) + "-" + str(dateTimeObj.day) + "-" + str(dateTimeObj.year)
    return time, date

def check_suspension(username, dateOfMessage):
    """
    Checks if suspension exists for given user
    Args:
        username : the username of the user to be checked
    Returned:
        0 if doesn't exist, 1 if does exist
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT people.ID FROM people WHERE people.username = '%s'""" % (username))
    results = cur.fetchall()
    st = [item[0] for item in results]
    userID = st[0]

    cur.execute("""SELECT COUNT(*) FROM suspension WHERE suspension.userID = '%s'""" % (userID))
    results = cur.fetchall()
    st = [item[0] for item in results]

    #If suspension for user exists
    if(st[0] == 1):
        dateM = dateOfMessage.split('-')
        #print(dateM)

        cur.execute("""SELECT start FROM suspension WHERE suspension.userID = '%s'""" % (userID))
        results = cur.fetchall()
        et = [item[0] for item in results]
        startSus = et[0].split('-')
        #print(startSus)

        cur.execute("""SELECT expiration FROM suspension WHERE suspension.userID = '%s'""" % (userID))
        results = cur.fetchall()
        et = [item[0] for item in results]
        endSus = et[0].split('-')
        #print(endSus)

        #Checks if date falls in between years :: Returns after all other statements
        if(int(dateM[2]) >= int(startSus[2]) and int(dateM[2]) <= int(endSus[2])):
            #If the year falls in between the years and is not equal to either
            if(int(dateM[2]) > int(startSus[2]) and int(dateM[2]) < int(endSus[2])):
                return 1
            #If the year is the same as the starting year and less than the end year
            elif(int(dateM[2]) == int(startSus[2]) and int(dateM[2]) < int(endSus[2])):
                #Is the month before the starting month?
                if(int(dateM[0]) < int(startSus[0])):
                    return 0
                #Is the month after the starting month?
                elif(int(dateM[0]) > int(startSus[0])):
                    return 1
                #Is the month the same?
                else:
                    #Is the day before the starting day?
                    if(int(dateM[1]) < int(startSus[1])):
                        return 0
                    #Is the day after or equal to the starting day?
                    else:
                        return 1
            #If the year is greater than the starting year and equal to the end year
            elif(int(dateM[2]) > int(startSus[2]) and int(dateM[2]) == int(endSus[2])):
                #Is the month after the end month?
                if(int(dateM[0]) > int(endSus[0])):
                    return 0
                #Is the month before the end month?
                elif(int(dateM[0]) < int(endSus[0])):
                    return 1
                #Is the month the same?
                else:
                    #Is the day after the end day?
                    if(int(dateM[1]) > int(endSus[1])):
                        return 0
                    #Is the day before or equal to the end day?
                    else:
                        return 1
            #If the year for all of the above is the same
            else:
                #Is the month before the start or after the end?
                if(int(dateM[0]) < int(startSus[0]) or int(dateM[0]) > int(endSus[0])):
                    return 0
                #Is the month after the start and before the end?
                elif(int(dateM[0]) > int(startSus[0]) and int(dateM[0]) < int(endSus[0])):
                    return 1
                #Is the month the same as the start and before the end?
                elif(int(dateM[0]) == int(startSus[0]) and int(dateM[0]) < int(endSus[0])):
                    #If the day is the same or after the start day
                    if(int(dateM[1]) >= int(startSus[1])):
                        return 1
                #Is the month after the start and the same as the end?
                elif(int(dateM[0]) > int(startSus[0]) and int(dateM[0]) == int(endSus[0])):
                    #If the day is the same or before the end day
                    if(int(dateM[1]) <= int(endSus[1])):
                        return 1
                #Is the month the same for all of the above?
                else:
                    #Is the day before the start or after the end?
                    if(int(dateM[1]) >= int(startSus[1]) and int(dateM[1]) <= int(endSus[1])):
                        return 1

            return 0



    conn.close()
    return 0

#Need to check if suspension exists for sender
def send_new_message(new_message, recipient, sender, dateOfMessage):
    """
    Sends a new message if no suspension for the user exists
    Args: 
        new_message : The message to be sent
        recipient : The user who is receiving the message
        sender : The user who is sending the message
    Returned:
        ERROR if a suspension exists, None if successful
    """

    conn = connect()
    cur = conn.cursor()

    if(check_suspension(sender, dateOfMessage)):

        cur.execute("""SELECT people.ID FROM people WHERE people.username = '%s'""" % (sender))
        results = cur.fetchall()
        userID = [item[0] for item in results]

        cur.execute("""SELECT suspension.expiration FROM suspension WHERE suspension.userID = '%s'""" % (userID[0]))
        results = cur.fetchall()
        st = [item[0] for item in results]

        raise Exception("User is suspended from sending messages until '%s'" % (st[0]))

    

    status = "Unread"
    id_status = 1

    cur.execute("""SELECT COUNT(messages.chatID) FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (sender, recipient))
    results = cur.fetchall()
    existingConvo = [item[0] for item in results]
    curr = existingConvo[0]

    if(curr == 0):
        id_status = 2
        cur.execute("""SELECT COUNT(messages.chatID) FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (recipient, sender))
        results = cur.fetchall()
        newEC = [item[0] for item in results]
        curr = newEC[0]

    #Gets chat ID for conversation
    # No solutions for conversations which have not yet been started
    if(curr == 0):
        cur.execute("""SELECT DISTINCT messages.chatID FROM messages""")
        results = cur.fetchall()
        numOfChats = [item[0] for item in results]
        chatID = str(len(numOfChats) + 1)

    else:
        if(id_status == 1):
            cur.execute("""SELECT messages.chatID FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (sender, recipient))
            results = cur.fetchall()
            chatID_sol = [item[0] for item in results]
            chatID = chatID_sol[0]
        else:
            cur.execute("""SELECT messages.chatID FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (recipient, sender))
            results = cur.fetchall()
            chatID_sol = [item[0] for item in results]
            chatID = chatID_sol[0]





    time, date = getTimeAndDate()

    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", (chatID, new_message, time, dateOfMessage, status, sender, recipient))


    conn.commit()
    conn.close()

def check_messages_from_user(user, sender):
    """
    Gets all the messages to a user from a sender
    Args: 
        user : The user who is receiving the messages
        sender : The user who is sending the messages
    Returned:
        A list of all of the messages to a user from a sender
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT messages.message FROM messages WHERE messages.sender = (%s) AND messages.receiver = (%s)""", (sender, user))
    results = cur.fetchall()
    all_messages_from_sender = [item[0] for item in results]
    
    conn.commit()
    conn.close()
    
    return all_messages_from_sender

    


def check_messages(user):
    """
    Gets all users who have sent messages to a user
    Args: 
        user : The user that is receiving these messages
    Returned:
        A list of all of the users who have sent messages to the specified user
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT DISTINCT messages.sender FROM messages WHERE messages.receiver = '%s'""" % (user))
    results = cur.fetchall()
    all_messages_for_user = [item[0] for item in results]

    conn.commit()
    conn.close()

    return all_messages_for_user

def get_count_unread(user):
    """
    Gets a count of all unread messages to a user for direct messages
    Args: 
        user : The user of the unread messages
    Returned:
        The number of unread messages to a user
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT COUNT(messages) FROM messages WHERE messages.receiver = '%s' AND messages.status = 'Unread'""" % (user))
    results = cur.fetchall()
    all_messages_for_user = [item[0] for item in results]

    conn.commit()
    conn.close()

    return all_messages_for_user


def mark_message_read(user, message, sender):
    """
    Marks the specified message as read
    Args: 
        user : The acting user that is reading the message
        message : The message that is being read
        sender : The sender of the message
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""UPDATE messages SET status = 'Read' WHERE messages.message = '%s' AND messages.receiver = '%s' AND messages.sender = '%s'""" % (message, user, sender))

    conn.commit()
    conn.close()


def check_user_change(username, date):
    """
    Checks if a username has been changed in the last 6 months
    Args: 
        username : The user we are checking for a change
    Returned:
        An integer where 0 represents no and 1 represents yes
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT people.username_change FROM people WHERE people.username = '%s'""" % (username))
    results = cur.fetchall()
    st = [item[0] for item in results]
    chDate = st[0].split('-')

    currDate = date.split('-')

    conn.close()

    monthDifference = ((int(currDate[2]) - int(chDate[2])) * 12) + int(currDate[0]) - int(chDate[0])
    if(abs(monthDifference) < 6):
        #print("Less tha 6 months")
        return 1
    elif(abs(monthDifference) == 6 and int(currDate[1]) < int(chDate[1])):
        #print("6months not days tho")
        return 1
    
    #print("More than 6 months")
    return 0


    

#As for the 6 month period, may add updated date to the people table to determine if it has been six months since it was updated
def update_username(current_user, new_username, date):
    """
    Updates the username if the username has not been updated in the past 6 months
    Args: 
        current_user : the current username of the actor
        new_username : the desired username change
    Returned:
        None
    """
    if(check_user_change(current_user, date) == 1):
        raise Exception("Username cannot be changed more than once in 6 months")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""UPDATE people SET username = '%s' WHERE people.username = '%s'""" % (new_username, current_user))

    cur.execute("""UPDATE conversation SET user1 = '%s' WHERE conversation.user1 = '%s'""" % (new_username, current_user))
    cur.execute("""UPDATE conversation SET user2 = '%s' WHERE conversation.user2 = '%s'""" % (new_username, current_user))

    cur.execute("""UPDATE messages SET sender = '%s' WHERE messages.sender = '%s'""" % (new_username, current_user))
    cur.execute("""UPDATE messages SET receiver = '%s' WHERE messages.receiver = '%s'""" % (new_username, current_user))

    #Community Updates

    cur.execute("""UPDATE community_channels SET sender = '%s' WHERE community_channels.sender = '%s'""" % (new_username, current_user))

    #Get a list of existing communities
    cur.execute("""SELECT DISTINCT community_name FROM community""")
    results = cur.fetchall()
    all_comms = [item[0] for item in results]

    for row in all_comms:
        cur.execute("""SELECT community.community_suspended_users FROM community WHERE community_name = '%s'""" % (row))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_sus_members = st[0].split(',')

        if(current_user in curr_sus_members):
            curr_sus_members.remove(current_user)
            curr_sus_members.append(new_username)
            new_curr_members = ','.join(map(str, curr_sus_members))
            cur.execute("""UPDATE community SET community_suspended_users = '%s' WHERE community_name = '%s'""" % (new_curr_members, row))
        
        cur.execute("""SELECT community.community_members FROM community WHERE community_name = '%s'""" % (row))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_members = st[0].split(',')

        if(current_user in curr_members):
            curr_members.remove(current_user)
            curr_members.append(new_username)
            new_curr_members = ','.join(map(str, curr_members))
            cur.execute("""UPDATE community SET community_members = '%s' WHERE community_name = '%s'""" % (new_curr_members, row))

    #Update userchange date
    cur.execute("""UPDATE people SET username_change = '%s' WHERE people.username = '%s'""" % (date, new_username))

    conn.commit()
    conn.close()

def account_suspension(action, userID, endDate="NULL", endYear="NULL"):
    """
    Dependent upon the action, a user can be either suspended or cleared from suspension
    Args: 
        action : Can be either 'Suspend' or 'Clear'.  Determines action of this method
        userID : The id of the user associated with the action
        endDate : If the action is 'Suspend' the endDate is the date the suspension ends, NULL otherwise
        endYear : If the action is 'Suspend' the endYear is the year the suspension ends, NULL otherwise
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    if(action == "Suspend"):
        datetimeObj = datetime.now()
        startYear = str(datetimeObj.year)
        time, start = getTimeAndDate()
        cur.execute("INSERT INTO suspension (userID, start, expiration, startYear, endYear) VALUES (%s, %s, %s, %s, %s);", (userID, start, endDate, startYear, endYear))
    if(action == "Clear"):
        cur.execute("""DELETE FROM suspension WHERE userID = '%s'""" % (userID))

    conn.commit()
    conn.close()
    
def create_user(new_id, username, email, ssn, phone):
    """
    Creates a new user with the given arguments
    Args: 
        new_id : The ID of the new user
        username : The username of the new user
        email : The email of the new user
        ssn : the social security number of the new user
        phone : the phone number of the new user
    Returned:
        Error message if username is less than 8 characters
        None if successful
    """
    if(len(username) < 8):
        return "ERROR: New usernames must be at least 8 characters long"
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO people (ID, username, email, ssn, phone, username_change) VALUES (%s, %s, %s, %s, %s, %s);", (new_id, username, email, ssn, phone, '00-00-0000'))
    
    conn.commit()
    conn.close()

def read_csv_into_db(file):
    """
    Reads the given csv file 'whos_on_first.csv' into the database messages (Currently this is a static method made for this specific file)
    Args: 
        file : the given file to be read into the database
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    chatId = '1'
    stockTime = '00:00'
    stockDate = '01-01-2021'
    stockStatus = 'Unread'


    with open(file, 'r') as f:
        csv_reader = reader(f)
        head = next(csv_reader)

        if head != None:
            for row in csv_reader:
                if(row[0] == 'Abbott'):
                    sender = row[0]
                    receiver = 'Costello'
                    message = row[1]
                    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", (chatId, message, stockTime, stockDate, stockStatus, sender, receiver))

                if(row[0] == 'Costello'):
                    sender = row[0]
                    receiver = 'Abbott'
                    message = row[1]
                    cur.execute("INSERT INTO messages (chatID, message, time, date, status, sender, receiver) VALUES (%s, %s, %s, %s, %s, %s, %s);", (chatId, message, stockTime, stockDate, stockStatus, sender, receiver))


    conn.commit()
    conn.close()


def community_membership(choice, user, com_name):
    """
    Given choice, allows the user to join or leave a community
    Args:
        choice : 'Join' or 'Leave' string that determines functionality
        userID : the user attempting to perform this action
        com_name : the name of the community associated with this action
    Returned:
        None if successful
        Error if unsuccessful
    """
    conn = connect()
    cur = conn.cursor()

    if(choice == 'Join'):
        cur.execute("""SELECT community.community_members FROM community WHERE community_name = '%s'""" % (com_name))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_members = st[0].split(',')

        if(user not in curr_members):
            curr_members.append(user)
            new_curr_members = ','.join(map(str, curr_members))
            cur.execute("""UPDATE community SET community_members = '%s' WHERE community_name = '%s'""" % (new_curr_members, com_name))


    elif(choice == 'Leave'):
        cur.execute("""SELECT community.community_members FROM community WHERE community_name = '%s'""" % (com_name))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_members = st[0].split(',')

        if(user in curr_members):
            curr_members.remove(user)
            new_curr_members = ','.join(map(str, curr_members))
            cur.execute("""UPDATE community SET community_members = '%s' WHERE community_name = '%s'""" % (new_curr_members, com_name))

    else:
        return 'ERROR: Incorrect Command'

    conn.commit()
    conn.close()

def send_community_message(sender, com_name, chan, c_message):
    """
    Sends a community message if the sender is a member of the community
    Args:
        sender : the userID that is sending the message
        com_name : the name of the community where the message is being sent
        chan : the channel the message is being sent in
    Returned:
        None
    """
    conn = connect()
    cur = conn.cursor()

    #Check if the sender is a member of community prior to sending message in channel
    cur.execute("""SELECT community.community_members FROM community WHERE community_name = '%s'""" % (com_name))
    results = cur.fetchall()
    st = [item[0] for item in results]
    curr_members = st[0].split(',')
    if(sender not in curr_members):
        raise Exception("User is not a member of this channel")

    #Check if the sender is suspended from a community prior to sending message in channel
    cur.execute("""SELECT community.community_suspended_users FROM community WHERE community_name = '%s'""" % (com_name))
    results = cur.fetchall()
    st = [item[0] for item in results]
    curr_sus_members = st[0].split(',')
    if(sender in curr_sus_members):
        raise Exception("User is a suspended member of this channel")

    #Send the message
    time, date = getTimeAndDate()
    cur.execute("INSERT INTO community_channels (channel_name, community_name, sender, time, date, chan_message, status) VALUES (%s, %s, %s, %s, %s, %s, %s);", (chan, com_name, sender, time, date, c_message, 'Unread'))


    conn.commit()
    conn.close()


def get_count_unread_community(action, user, community='NULL', channel='NULL'):
    """
    Gets a count of unread messages from a community or channel dependent upon action
    Args:
        action : 'Community' or 'Channel' determines where the unread messages will come from
        user : The user who we are getting counts for
        community : required for channel as well as community, specifies the community in which the messages are found at
        channel : specifies the channel for which the counts come from
    Returned:
        An integer with the number of unread messages
    """
    conn = connect()
    cur = conn.cursor()

    if(action == 'Community'):
        cur.execute("""SELECT community.community_channels FROM community WHERE community_name = '%s'""" % (community))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_com = st[0].split(',')
        #print(curr_com)
        total_count = 0

        for row in curr_com:
            cur.execute("""SELECT COUNT(chan_message) FROM community_channels WHERE status = 'Unread' AND community_name = '%s' AND channel_name = '%s'""" % (community, row))
            results = cur.fetchall()
            xt = [item[0] for item in results]
            total_count = total_count + xt[0]
        
        conn.close()

        return total_count


    elif(action == 'Channel'):
        cur.execute("""SELECT COUNT(chan_message) FROM community_channels WHERE status = 'Unread' AND community_name = '%s' AND channel_name = '%s'""" % (community, channel))
        results = cur.fetchall()
        st = [item[0] for item in results]

        conn.close()

        return st[0]

    else:
        conn.close()
        raise Exception("Incorrect use of function")


def get_mentions(user):
    conn = connect()
    cur = conn.cursor()

    mention_string = '@' + user

    #Get a list of existing communities
    cur.execute("""SELECT DISTINCT community_name FROM community""")
    results = cur.fetchall()
    all_comms = [item[0] for item in results]

    #Check for member not within communities (Remove communities from all_coms if not a member)
    for row_mem in all_comms:
        cur.execute("""SELECT community_members FROM community WHERE community_name = '%s'""" % (row_mem))
        results = cur.fetchall()
        st = [item[0] for item in results]
        all_mem = st[0].split(',')
        if(user not in all_mem):
            all_comms.remove(row_mem)


    #Get mentions

    all_mentions = []

    for row in all_comms:
        cur.execute("""SELECT community_channels FROM community WHERE community_name = '%s'""" % (row))
        results = cur.fetchall()
        st = [item[0] for item in results]
        all_chans = st[0].split(',')
        for row_chan in all_chans:
            cur.execute("""SELECT chan_message FROM community_channels WHERE community_name = '%s' AND channel_name = '%s'""" % (row, row_chan))
            results = cur.fetchall()
            all_mess = [item[0] for item in results]
            for row_mess in all_mess:
                if(mention_string in row_mess):
                    all_mentions.append(row_mess)


    conn.close()

    return all_mentions

def suspend_community(action, user, com_name):
    """
    Suspends or removes suspension for a user from a community
    Args:
        action : 'Suspend' or 'Remove' determines action for function
        user : The user to be suspended
        com_name : the community related to the suspension
    Returns:
        None
    """
    conn = connect()
    cur = conn.cursor()

    if(action == 'Suspend'):
        cur.execute("""SELECT community.community_suspended_users FROM community WHERE community_name = '%s'""" % (com_name))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_members = st[0].split(',')

        if(user not in curr_members):
            curr_members.append(user)
            new_curr_members = ','.join(map(str, curr_members))
            cur.execute("""UPDATE community SET community_suspended_users = '%s' WHERE community_name = '%s'""" % (new_curr_members, com_name))
    
    elif(action == 'Remove'):
        cur.execute("""SELECT community.community_suspended_users FROM community WHERE community_name = '%s'""" % (com_name))
        results = cur.fetchall()
        st = [item[0] for item in results]
        curr_members = st[0].split(',')

        if(user in curr_members):
            curr_members.remove(user)
            new_curr_members = ','.join(map(str, curr_members))
            cur.execute("""UPDATE community SET community_suspended_users = '%s' WHERE community_name = '%s'""" % (new_curr_members, com_name))

    else:
        raise Exception('Incorrect Usage of Function')

    conn.commit()
    conn.close()
    

def get_channels_community(community):
    """
    Gets a list of channels within a community
    Args:
        community : The community containing said channels
    Returns:
        A list of channels within a community
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT community_channels FROM community WHERE community_name = '%s'""" % (community))
    results = cur.fetchall()
    st = [item[0] for item in results]
    
    conn.close()

    return st[0].split(',')


def get_communities():
    """
    Gets a list of all communities
    Args:
        None
    Returns:
        A list of communities
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT community_name FROM community""")
    results = cur.fetchall()
    st = [item[0] for item in results]
    
    conn.close()

    return st


def search_community_message(community, mes):
    """
    Searches a community for a given message
    Args:
        community : the community to search in
        mes : the message string that is being searched for
    Returns:
        Returns all messages with the string within
    """
    conn = connect()
    cur = conn.cursor()

    all_words = mes.split(" ")
    word_string = all_words[0]

    if(len(all_words) > 1):
        for row_word in all_words[1:]:
            word_string = word_string + """ & """ + row_word

    cur.execute("""SELECT chan_message FROM community_channels WHERE to_tsvector(chan_message) @@ to_tsquery('%s')""" % (word_string))
    results = cur.fetchall()
    st = [item[0] for item in results]
    
    conn.close()
    
    return st

def moderator_query(sDate, eDate='None'):
    """
    Lists all users who have sent a message in a given date range who are currently suspended from any community
    Args: 
        sDate : Start date of given date range
        eDate : End date of given date range
                Defaults to current date
    Returns:
        A list of users
    """
    conn = connect()
    cur = conn.cursor()

    all_coms = get_communities()
    all_suspended_users = [] 
    mes_sent_sus_user = []

    if(eDate == 'None'):
        time, date = getTimeAndDate()
        eDate = date


    for com in all_coms:
        cur.execute("""SELECT community_suspended_users FROM community WHERE community_name = '%s'""" % (com))
        results = cur.fetchall()
        st = [item[0] for item in results]
        sus_user = st[0].split(",")
        for sender in sus_user:
            if(sender not in all_suspended_users and sender != ''):
                all_suspended_users.append(sender)

    for sender in all_suspended_users:
        cur.execute("""SELECT sender, date FROM community_channels WHERE sender = '%s'""" % (sender))
        results = cur.fetchall()

        for mes in results:
            if(check_date_inbetween(mes[1], sDate, eDate) and mes[0] not in mes_sent_sus_user):    
                mes_sent_sus_user.append(mes[0])
    
    conn.close()

    return mes_sent_sus_user

def get_user_suspended(com):
    """
    Checks if user is suspended from a community
    Args:
        com : The community being checked
    Returns:
        A list of suspended users
    """
    conn = connect()
    cur = conn.cursor()

    all_suspended_users = []

    cur.execute("""SELECT community_suspended_users FROM community WHERE community_name = '%s'""" % (com))
    results = cur.fetchall()
    st = [item[0] for item in results]
    sus_user = st[0].split(",")
    for sender in sus_user:
        if(sender not in all_suspended_users and sender != ''):
            all_suspended_users.append(sender)

    conn.close()
    
    return all_suspended_users



def activity_summary(given_date='None'):
    """
    Gives a breakdown of communities
    Args:
        given_date : A date that specifies the end of the 30 day period we are searching in
                     Defaults to current Date
    Returns:
        A list containing a breakdown of each community
    """
    conn = connect()
    cur = conn.cursor()

    temp_table = """
        CREATE TEMP TABLE temp_table(
            community varchar(255),
            avg_num_messages varchar(255),
            active_users varchar(255)
        )
    """

    cur.execute(temp_table)

    if(given_date == 'None'):
        time, date = getTimeAndDate()
        given_date = date

    dateTimeObj = datetime.now() - timedelta(days=30)
    start_date = str(dateTimeObj.month) + "-" + str(dateTimeObj.day) + "-" + str(dateTimeObj.year)
    
    all_coms = get_communities()

    for com in all_coms:
        cur.execute("""SELECT chan_message, date, sender FROM community_channels WHERE community_name = '%s'""" % (com))
        results = cur.fetchall()

        res_mes = []
        dist_users = []

        for mes in results:
            #print("Length of Message: ", len(mes[0]))
            #print("Message: ", mes[0])
            if(len(mes[0]) > 4 and check_date_inbetween(mes[1], start_date, given_date)):
                res_mes.append(mes)

                if(mes[2] not in dist_users):
                    dist_users.append(mes[2])
            
        act_users = len(dist_users)
        #print("Active Users: ", act_users)
        avg_num_mes = round(len(res_mes) / 30, 3)
        #print("Avg num Users: ", avg_num_mes)

        cur.execute("INSERT INTO temp_table (community, avg_num_messages, active_users) VALUES (%s, %s, %s);", (com, avg_num_mes, act_users))

    cur.execute("""SELECT * FROM temp_table""")
    results = cur.fetchall()

    conn.close()
    return results

    