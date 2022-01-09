# Skytale encryption
Encrypt/Decrypt text with Skytale method
---------------
## Usage
Clone repository:
````
git clone
cd skytale_encryption
````
For Encryption:
````
python3 skytale.py -enc <TextToEncrypt> -n <NumberOfTurns>
````
For Decryption:
````
python3 skytale.py -dec <TextToDecrypt> -n <NumberOfTurns>
````

### Example:
````
python3 skytale.py -enc 'That is a test' -n 5
Result: Tithsea stat  .

python3 skytale.py -dec 'Tithsea stat  .' -n 5
Result: That is a test.
````
For contribution just open an issue.
