const express = require('express');
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const app = express();
const port = 5000;

app.use(bodyParser.json()); // Middleware to parse JSON requests

mongoose.set("strictQuery", false);
const mongoDB = "mongodb connection string";

main().catch((err) => console.log(err));
async function main() {
  await mongoose.connect(mongoDB);
  console.log("Connected to MongoDB!");
}

// Define Schema
const fortuneSchema = new mongoose.Schema({
  name: String
});

// Create Model
const Fortune = mongoose.model("fortune", fortuneSchema);


// API Routes

// GET: Fetch all items
app.get('/api', async (req, res) => {
  try {
    const fortunes = await Fortune.find();
    res.json(fortunes);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// POST: Add a new item
app.post('/api', async (req, res) => {
  try {
    const newfortune = new Fortune({
      name: req.body.name
    });

    const savedFortune = await newfortune.save();
    res.status(201).json(savedFortune);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.listen(port, () => {
  console.log('API listening on port ' + port);
});

