from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv,"connected") #first time server says something back, this is intro
    #if recv[:3] != '220':
      #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n' # = helo crepes
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1,"HELLO") #server says hello nice meeting you
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailCommand = 'MAIL FROM: <eh2786@nyu.edu>\r\n' #client says i'm sending mail from here
    clientSocket.send(mailCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2,"mail from") #server says 250 sender name ok if good
    #if recv2[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptCommand = 'RCPT TO: <hamaerisu@gmail.com>\r\n' #client says i'm sending mail TO here
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3, "receipt to") #server says ok destination looks good
    #if recv3[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'  #i'm sending data
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4,"data will be sent") #ok make sure to send it w a period
    #if recv4[:3] != '354':
        #print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    #print(msg)
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    #print(endmsg)
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5, "got your message, will deliver")
    #if recv5[:3] != '250':
        #print('250 reply not received from server.')

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6, "closing connection")
    #if recv6[:3] != '221':
       #print('221 reply not received from server.')
    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

    #print("entire function run")
