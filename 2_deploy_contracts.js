var ElectionsContract = artifacts.require("./Election.sol");
module.exports = function(deployer) {
  deployer.deploy(ElectionsContract);
};