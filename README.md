# wolframalpha-bot
> A simple Flask app that provides a webhook for Slack to query the WolframAlpha API

## Setup

1. Configure the Flask App using your [WolframAlphaAPIKey](http://products.wolframalpha.com/api/):
```bash
export API_KEY=<WolframAlphaAPIKey>
export TOKEN=<MakeALongTokenToSendWithYourRequests>
```

2. Configure an [Outgoing WebHook](https://slack.com/apps/A0F7VRG6Q-outgoing-webhooks) for Slack with your `URL` and `TOKEN`.

3. Start app
  - production: run `gunicorn app:app`
  - development: run `python app.py`
