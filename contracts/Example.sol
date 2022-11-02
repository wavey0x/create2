pragma solidity ^0.8.0;

contract ExampleContract {
    
    event ValueChanged(string oldValue, string newValue);
    string public value;
    uint public makeUnique = 123456654321;
    
    function setValue(string memory _value) public {
        emit ValueChanged(value, _value);
        value = _value;
    }
}