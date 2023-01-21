import express from "express";
import { createServer } from "http";
import { Server } from "socket.io";
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// const { MongoClient } = require("mongodb");

// const DB = "mydb";
// const COLLECTION = "socket.io-adapter-events";


// const mongoClient = new MongoClient("mongodb://localhost:27017/?replicaSet=rs0", {
//   useUnifiedTopology: true,
// });

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, { /* options */ });
const port = 3000 ;

app.get('/', (req, res) => {
    res.sendFile(__dirname+ '/index.html');
  });
  
io.on("connection", (socket) => {
  // ...
  console.log('user connected');

});

io.engine.on("connection_error", (err) => {
    console.log(err.req);      // the request object
    console.log(err.code);     // the error code, for example 1
    console.log(err.message);  // the error message, for example "Session ID unknown"
    console.log(err.context);  // some additional error context
});
  
httpServer.listen(port , (err)=>{
    if (err) {
        console.log("Something went wrong");
        console.log(err);
    }
    
    console.log(`server has been started on ${port}`);
});
