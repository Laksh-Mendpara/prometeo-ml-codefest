import { google } from 'googleapis';
import User from '../models/User.js';
import "dotenv/config"
import { formatResponse } from '../utils/formatResponse.js';
import { generateToken } from '../utils/jwtUtils.js';

const OAuth2 = google.auth.OAuth2;

const oauth2Client = new OAuth2(
    process.env.GOOGLE_CLIENT_ID,
    process.env.GOOGLE_CLIENT_SECRET,
    process.env.GOOGLE_REDIRECT_URI
);

export const loginWithGoogle = (req, res) => {
    const scopes = [
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/userinfo.email',
    ];

    const url = oauth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: scopes,
        prompt: 'consent',
    });

    res.redirect(url);
}

export const callback = async (req, res) => {
    try {
        const { code } = req.query;
        const { tokens } = await oauth2Client.getToken(code);
        oauth2Client.setCredentials(tokens);

        const oauth2 = google.oauth2({
            auth: oauth2Client,
            version: "v2",
        });
        const userInfo = await oauth2.userinfo.get();

        let user = await User.findOneAndUpdate(
            { email: userInfo.data.email },
            {
                email: userInfo.data.email,
                username: userInfo.data.name,
                googleOAuthTokens: tokens,
            },
            { upsert: true, new: true },
        );

        const userToken = generateToken(user);
        user.token = userToken;
        await user.save();

        res.json(
            formatResponse(
                true,
                { message: "Authentication successful", userToken },
                null,
                null
            )
        );


    } catch (error) {
        console.error("Error during OAuth callback:", error);
        res
            .status(500)
            .json(formatResponse(false, null, 500, "Authentication failed"));
    }
} 