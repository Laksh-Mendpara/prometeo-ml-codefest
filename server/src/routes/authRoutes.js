import express from "express";
import { callback, loginWithGoogle } from "../controllers/authController.js";
import { verify } from "../middlewares/authMiddleware.js";


const router = express.Router();

router.get("/google/login", loginWithGoogle);
router.get("/google/callback", callback);

router.get("/debug", verify, (req, res) => {
    res.json({
        message: "debug route accessed",
        user: req.user,
    });
});

export default router;