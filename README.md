<p align="center"> <img src="Project Elements/Universal_Payment_Processor.png"/> </p>

<hr>
<br/>

Although relatively outdated,```UPP``` is the most comprehensive list of payment processing gateways utilizing the Bitcoin, Ethereum, and Ethereum Classic blockchains along with Cashapp.

## Use Case
As a digital entrepreneur, one of the most important things is being able to be compensated for your work. These reference code snippets provide ways to implement a payment gateway in whatever product you might choose to create virtually. At the time, 17-year-old Angafor *allegedly* used these payment gateways to enable automatic currency conversion with a 10-15% markup rate.

## Usage
These are purely to serve as reference. From what I understand, the CashApp gateway is severely flawed.


## Cashapp Payment Processor

Unlike the crypto gateways, the CashApp process was unique to my thought process at the time so I will provide some explanation. The cashapp payment processor works by scrapping a user's email address for emails from cashapp. If any are present, it checks if it's an incoming or outgoing payment. If it is an incoming payment, the program appends the cashtag of the sender, the amount received, and the time of the transaction to an SQLite database. The program also appends the receipt of the received transaction to a text file so when scanning your email inbox again, it skips over old received payments. Adding to this, there can be only one received payment from a user at a time. If an old payment is still in the database, it is overwritten by the new one. You (as a developer) can utilize this by checking the database for any payments from a user and then performing some action if the payment is present. I have included the code to perform the check and delete the payment once the good has been dispensed to the user.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
<br/>
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
