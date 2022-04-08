# AcceptingCryptoPayments

# Testing

Unfortunately, Coinbase Commerce doesn't support sandbox accounts for testing, which means that you'll need to use real crypto to test your application.

With the server running, navigate to http://localhost:8000/. You can test using the Coinbase hosted site or the embedded checkout. Your choice.

When you select a cryptocurrency with which you'd like to pay, a wallet address (and a QR code) will be shown.

You then have 60 minutes to transfer the crypto before the charge times out.

After you send the crypto, it will take a few minutes (depending on which cryptocurrency you use) for miners to confirm your transaction. After the transaction gets the required number of confirmations (based on the cryptocurrency), you'll be presented with a "Payment complete" message.

The payments will appear in the Commerce Dashboard under "Payments" section.

# Confirm Payments with Webhooks

go to "ConfirmPaymentsWithWebhooks" branch
