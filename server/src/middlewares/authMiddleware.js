import { verifyToken } from "../utils/jwtUtils.js";
import User from "../models/User.js";

export const verify = async (req, res, next) => {
    try {
        const token = req.headers.authorization?.split(" ")[1];
        if (!token) throw new Error("Not authorized, no token");

        const decoded = verifyToken(token);

        const user = await User.findById(decoded.id);
        if (!user) throw new Error("User not found");
        req.user = user;
        next();
    } catch (error) {
        res.status(401).json({ message: error.message || "Not authorized" });
    }
}