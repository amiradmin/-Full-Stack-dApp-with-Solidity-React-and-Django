const { ethers } = require("hardhat");

async function main() {
    const Transaction = await ethers.getContractFactory("Transaction");
    const transaction = await Transaction.deploy();

    await transaction.waitForDeployment();  // ✅ Replaces deployed()

    console.log(`Contract deployed at: ${await transaction.getAddress()}`);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
