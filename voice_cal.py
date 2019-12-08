from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    
    fromNo = request.values["from"]

    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say('Hi , Thanks for calling PayPal offline payment service, {}'.format(fromNo), voice='alice')

    resp.hangup()

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
