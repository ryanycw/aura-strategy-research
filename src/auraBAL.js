require("dotenv/config");
const fs = require('fs');
const cliProgress = require('cli-progress');
const { ethers, Wallet } = require("ethers");
const provider = new ethers.providers.JsonRpcProvider(process.env.INFURA_MAINNET_URL);
const walletPrivateKey = new Wallet(process.env.PK1);
const signer = walletPrivateKey.connect(provider);
const result = {"balancesList":[]};
const contractFile = require("../import/abi/BaseRewardPool.json");
const depositList = require("../import/80BAL-20WETH-depositList.json")

async function main() {
    console.log("Making signatures with the account:", (await signer.getAddress()));
    console.log("Account balance:", (await signer.getBalance()).toString());
    
    factory = new ethers.ContractFactory(contractFile.abi, contractFile.bytecode, signer);
    reward = await factory.attach(process.env.AURABAL_REWARD_CONTRACT_MAINNET);
    console.log("Token Address: ", reward.address);
    const totalDepositListLen = depositList.record.length
    
    const bar1 = new cliProgress.SingleBar({}, cliProgress.Presets.shades_classic);
    bar1.start(totalDepositListLen,0);
    for(let i=0; i<totalDepositListLen; i++) {
        bar1.increment();
        const depositBalance = await reward.balanceOf(depositList.record[i].address);
        if (ethers.BigNumber.from(depositBalance).gt(ethers.BigNumber.from('0'))) {
            const outputData = {address: depositList.record[i].address,
                                totalBalance: ethers.utils.formatEther(ethers.BigNumber.from(depositBalance).toString())};
            result["balancesList"].push(outputData);
        }
    }
    bar1.stop();

    fs.writeFileSync('./out/80BAL-20WETH-deposit.json', JSON.stringify(result));
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
});