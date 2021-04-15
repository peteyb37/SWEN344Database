Reactions
-------------
If we were to include reactions, I would start by editing the messages table and the community_channels table
to include reaction (yes or no).  I would then link each individual message to a reactions table.
This table would include the message, the sender, the date, the channel (if applicable), the community (if applicable), 
the reaction itself, and the person who is reacting.  There could be multiple entries in the table for each 
message if it were reacted to more than once.

I would add an API method for reacting to a message.  Given the message, channel (if applicable), community (if applicable),
sender, reaction, and the person who is reacting; a new entry to the reaction table would be created and in UI, if the message 
has a yes under reactions, a little infographic would pop up and you could see the reactions.

Existing API methods would really only have to change for entries into the messages or community_channels tables.  These would
simply have to include the message to be created with 'no' in the  reaction section on creation.


Threaded Conversations
-------------
I am assuming that this would not be needed in direct messaging.  If we wanted to do threaded in the community channels, 
I would simply add an ID to each message and any message that is a reply to another, would have the same replyID.  The first 
message with that ID would be the original message and all after it would be replys in that conversation.  
We could also create an entire reply messages table, but I would think that might be overkill unless we wanted to expand into
multi-threaded conversations.

I would add either add an API or change the send message for communities method to include an action statement.  This action
statement would be either new_message or reply_message and it would find the message in the table, get the ID of that message 
and adopt it as its own ID when put into the table.

Existing API methods would have to account for the replyID in the community_channels table.