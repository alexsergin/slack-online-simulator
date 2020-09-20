# Slack Online Simulator

If you need to be online in Slack but you can't then just start this online simulator and that's done:)

You need Docker to use this tool. Install the Docker and just exec the following command:
```bash
docker run --rm --name slack-online-simulator -e WORKSPACE_URL=https://YOUR_COMANY.slack.com -e AUTH_EMAIL=YOUR_SLACK_EMAIL -e AUTH_PASSWORD=YOUR_SLACK_PASSWORD alexsergin/slack-online-simulator
```

You can also specify end work hour and minutes with `END_HOUR` and `END_MINUTES` env variables.
You can set an interval for `END_MINUTES` as `FROM:TO` like `30:59`.
In that case client will choose random value from the interval and stop in different time.
If you'll set just a single minute the client stop in specified minute all time. 