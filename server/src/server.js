import app from "./app.js";
import connectDB from "./db/db.js";
import "dotenv/config"

connectDB()
    .then(() => {
        app.listen(process.env.PORT || 5001)
        console.log(`Server running at port = ${process.env.PORT || 5001}`)
    })

    .catch((error) => {
        console.log(`\nMongoDB Connection failed\n`, error)
    })
