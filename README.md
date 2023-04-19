# Document-Encryptor-Decryptor
This program can be used to Encrypt and Decrypt personal documents.

#### Requirments

This program requires Python and Cryptography... pip install cryptography

#### Uses

This program will read and write to documents in its current directory and sub-folders.
It will generate its own base64 32 character key and save it to 'key.key' in it's current
directory for future use. It will also list all documents and ask the user to select a number
correlating to the document the user wants to encrypt or decrypt and also allow the user to 
choose if they want to encrypt or decrypt the document using the generated key. The chosen 
document will be encrypted or decrypted depending on what the user chooses.

This program was developed to help secure personal information on the users device incase
of a data breach to protect personal information.

#### Notes

To ensure that documents are well protected it is sugested that it is used on an external storage 
device such as USB, exteranl SSD or HDD so the documents and key are not accessable unless needed
by the user.
