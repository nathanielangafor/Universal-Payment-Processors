# Payment-Processors

Payment processors for Bitcoin, Ethereum, Ethereum Classic, and Cashapp. They are set up as functions for easy plugins/use.



My #1 priority in everything I do is efficiency. Nothing is more efficient than autonomy so I found myself using these quite a lot and thought I would share them in case anyone out there needs them.



<h1> Cryptocurrency Payment Processors </h1>

These payment processors are extremely easy to replicate and are usually 10-15 lines of code. They work by checking the blockchain for received payments. At the time of writing this program, the cryptocurrency payment processor is protected from the 'Low Fee Scam' where users send really low fees (1-3 Satoshi in the case of bitcoin) which cause the payment to be rejected. The processor returns false until the payment is confirmed.



<h1> Cashapp Payment Processor </h1>

The cashapp payment processor works by scrapping a user's email address for emails from cashapp. If any are present, it checks if it's an incoming or outgoing payment. If it is an incoming payment, the program appends the cashtag of the sender, the amount received, and the time of the transaction to an SQLite database. The program also appends the receipt of the received transaction to a text file so when scanning your email inbox again, it skips over old received payments. Adding to this, there can be only one received payment from a user at a time. If an old payment is still in the database, it is overwritten by the new one. You (as a developer) can utilize this by checking the database for any payments from a user and then performing some action if the payment is present. I have included the code to perform the check and delete the payment once the good has been dispensed to the user.

<h1> DISCLAIMER </h1>

This was a program made just for fun I do not recommend using this on a large-scale project purely because I do not know if it can be exploited. Some precautions I took were checking if the payment came from the official Cashapp, and checking if the payment was recieved rather than pending.
