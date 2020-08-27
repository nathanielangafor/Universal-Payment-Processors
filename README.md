# Payment-Processors

Payment processors for Bitcoin, Ethereum, Ethereum Classic, and Cashapp. They are setup as functions for easy plugin/use.



My #1 priority in everything I do from business to fun is efficiency. Nothing is more efficient than autonomy so I found myself using these quite a lot and thought I share them in case anyone out there needs it.



<h1> Cryptocurrency Payment Processors </h1>

These payment processors are extremely easy to replicate and are usually 10-15 lines of code. They work by checking the blockchain for recieved payments. At the time of writting this program, the cryptocurrency payment processor is protected from the 'Low Fee Scam' where users send really low fees (1-3 Satoshi in the case of bitcoin) which cause the payment to be rejected. The processor returns false until the payment is confirmed.



<h1> Cashapp Payment Processor </h1>



>Background Info: Cashapp sends users an email confirmation when a payment is sent/received. 
>Rather than writting 50+ lines of code to check my gmail inbox I instead used the OneSecMail API which does it in line 5 lines. You need to add a One Sec Mail email to your cashapp account and put the email username into the program for it to work. I recommend using a 19 character username to lower the possibility of an exploit (0JONutOZP11AItKM6R1@1secmail.com)


The cashapp payment processor works by scrapping a user's email address for emails from cashapp. If any are present, it checks if its an incoming or outgoing payment. If it is an incoming payment, the program appends the cashtag of the sender, the amount received, and the time of the transaction to an SQLite database. The program also appends the receipt of the received transaction to a text file so when scanning your email inbox again, it skips over old received payments. Adding to this, there can be only one received payment from a user at a time. If an old payment is still in the database, it is overwritten by the new one. You (as a developer) can utilize this by checking the database for any payments from a user then performing some action if the payment is present. I have included the code to perform the check and delete the payment once the good has been dispensed to the user.

<h1> DISCLAIMER </h1>

This was obviously a program made just for fun I do not recommend using this on large scale project purely due to the fact that I do not know if it can be exploited. Some precautions I took were checking if the payment came from the official Cashapp, and checking if the payment was actually recieved rather than pending.
