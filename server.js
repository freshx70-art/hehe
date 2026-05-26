const express = require('express');
const app = express();
const port = 3000;

app.get('/get-roblox-cookie', (req, res) => {
    // Retrieve the .ROBLOSECURITY cookie from the request
    const robloxCookie = req.cookies['.ROBLOSECURITY'];
    if (robloxCookie) {
        res.json({ cookie: robloxCookie });
    } else {
        res.status(404).json({ error: 'Roblox cookie not found' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
