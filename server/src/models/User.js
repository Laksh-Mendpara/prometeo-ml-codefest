import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema(
    {
        username: {
            type: String,
            required: true,
            unique: true,
            lowercase: true,
            trim: true,
        },
        email: {
            type: String,
            required: true,
            unique: true,
            lowercase: true,
            trim: true,
        },
        googleOAuthTokens: { // for extra permissions
            type: Object,
            select: false,
        },
        token: {
            type: String,
            select: false,
        },
    },
    {
        timestamps: true,
    }
)

export default mongoose.model("User", UserSchema);