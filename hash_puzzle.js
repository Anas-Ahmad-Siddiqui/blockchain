// Anas Ahmad Siddiqui 20BPS1094
const prompt = require('prompt-sync')();

const SHA256 = require("crypto-js/sha256");

class Block {
  constructor(index, timestamp, data, previousHash = "") {
    this.index = index;
    this.timestamp = timestamp;
    this.data = data;
    this.previousHash = previousHash;
    this.hash = this.calculateHash();
    this.nonce = 0;
  }

  calculateHash() {
    return SHA256(
      this.index +
        this.previousHash +
        this.timestamp +
        JSON.stringify(this.data) +
        this.nonce
    ).toString();
  }

  mineBlock(difficulty) {
    while (
      this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")
    ) {
      this.nonce++;
      this.hash = this.calculateHash();
    }

    console.log("Block mined: " + this.hash);
  }
}

class Blockchain {
  constructor() {
    this.chain = [this.createGenesisBlock()];
    this.difficulty = 3;
  }

  createGenesisBlock() {
    return new Block(0, "02/01/2018", "Genesis Block", "0");
  }

  getlatestBlock() {
    return this.chain[this.chain.length - 1];
  }

  addBlock(newBlock) {
    newBlock.previousHash = this.getlatestBlock().hash;
    newBlock.mineBlock(this.difficulty);
    //newBlock.hash = newBlock.calculateHash();
    this.chain.push(newBlock);
  } //In reality we cannot add a new block so easily. There are numerous checks in place like 'Proof of work', 'Proof of stake' etc.

  isChainValid() {
    for (let i = 1; i < this.chain.length; i++) {
      const currentBlock = this.chain[i];
      const previousBlock = this.chain[i - 1];

      if (currentBlock.hash !== currentBlock.calculateHash()) {
        return false;
      } //check for hash calculations

      if (currentBlock.previousHash !== previousBlock.hash) {
        return false;
      } //check whether current block points to the correct previous block
    }

    return true;
  }
}

let koreCoin = new Blockchain();

const start = Date.now();

var var1 = prompt("cat1: ")
var var2 = prompt("cat2: ")
var var3 = prompt("cat3: ")

console.log("Mining block 1...");
koreCoin.addBlock(new Block(1, "01/01/2018", { cat1: var1, cat2: var2, cat3: var3 }));
console.log("Mining block 2...");
koreCoin.addBlock(new Block(2, "02/01/2018", { amount: 40 }));
console.log("Mining block 3...");
koreCoin.addBlock(new Block(3, "02/01/2018", { amount: 40 }));

const end = Date.now();
console.log(`Execution time: ${end - start} ms`);