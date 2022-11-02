pragma solidity ^0.8.0;

contract ExampleContract {
    
    event ValueChanged(string oldValue, string newValue);
    string public value;
    
    constructor(string memory _value) public {
        value = _value;
    }
    
    function setValue(string memory _value) public {
        emit ValueChanged(value, _value);
        value = _value;
    }
}