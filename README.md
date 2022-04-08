# AcceptingCryptoPayments

# Testing

Unfortunately, Coinbase Commerce doesn't support sandbox accounts for testing, which means that you'll need to use real crypto to test your application.

With the server running, navigate to http://localhost:8000/. You can test using the Coinbase hosted site or the embedded checkout. Your choice.

When you select a cryptocurrency with which you'd like to pay, a wallet address (and a QR code) will be shown.

You then have 60 minutes to transfer the crypto before the charge times out.

After you send the crypto, it will take a few minutes (depending on which cryptocurrency you use) for miners to confirm your transaction. After the transaction gets the required number of confirmations (based on the cryptocurrency), you'll be presented with a "Payment complete" message.

The payments will appear in the Commerce Dashboard under "Payments" section.

# Confirm Payments with Webhooks

Our app works well at this point, but we can't programmatically confirm payments yet. We just redirect the user to the success page after they check out, but we can't rely on that page alone since payment confirmation happens asynchronously.
(ie- the user might get redirected to the success page before their payment is confirmed and before we receive their funds.)

To get notified when the payment goes through, you need to create a webhook. We'll need to create a simple endpoint in our application, which Coinbase Commerce will call whenever an event occurs (i.e., when a charge is confirmed). By using webhooks, we can be sure the payment went through successfully.

# Register the Endpoint

Navigate to https://commerce.coinbase.com/dashboard/settings, scroll down to "Webhook subscriptions" and click on "Add an endpoint"
Enter your endpoint URL and press "Save".
Note - The URL needs to start with HTTPS, which means that you need to deploy your app before you can test it.

Add the shared secret to the settings.py file like so:
COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET = '<your coinbase webhook secret here>'

# Test the Endpoint

With your application deployed, you can send a test webhook request from the Commerce Dashboard. Navigate to "Webhook subscriptions" and click on "Details" under the webhook endpoint and Enter your endpoint URL and press "Save".

# My hosted website Link:

https://AcceptingCryptoPayments.shubhamkumar252.repl.co
