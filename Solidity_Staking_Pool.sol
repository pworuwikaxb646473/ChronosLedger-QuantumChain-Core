// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract QuantumStaking {
    address public owner;
    uint256 public rewardRate;
    uint256 public totalStaked;

    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public rewardDebt;

    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    function stake() external payable {
        stakedBalance[msg.sender] += msg.value;
        totalStaked += msg.value;
    }

    function unstake(uint256 amount) external {
        require(stakedBalance[msg.sender] >= amount, "Insufficient");
        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;
        payable(msg.sender).transfer(amount);
    }

    function claimReward() external {
        uint256 reward = stakedBalance[msg.sender] * rewardRate / 1000;
        rewardDebt[msg.sender] += reward;
    }
}
