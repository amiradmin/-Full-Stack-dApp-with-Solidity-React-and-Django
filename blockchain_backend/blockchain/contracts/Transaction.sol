// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Transaction Contract
 * @dev Stores and emits Ethereum transactions.
 */
contract Transaction {
    /// @notice Event emitted when a transaction is recorded.
    event TransactionRecorded(address indexed sender, uint256 value, string txHash);

    /**
     * @notice Records a new transaction.
     * @param _txHash The transaction hash.
     */
    function recordTransaction(string memory _txHash) public payable {
        require(msg.value > 0, "Transaction value must be greater than zero.");
        emit TransactionRecorded(msg.sender, msg.value, _txHash);
    }
}
