from cryptography.fernet import Fernet

# a='ddMOfTXmMqnATz2UzhKkADhPtWa3bwxdUpSIrJ4SyUM='
# key = Fernet.generate_key()
#
#gAAAAABnvZ-K2FU-o72gRBuNKnN23SkNjv_ne88o5cJVt8CbbQFt32U6wnrMqGH7HL8KBfhL8eKnSn3u32-LWm2bEymx0UuxJLD_IDMQo4_Y1vxPnH30eP0=
# print(key)

cipher_suite = Fernet('ddMOfTXmMqnATz2UzhKkADhPtWa3bwxdUpSIrJ4SyUM=')
# password = "MySecurePassword123"
# encrypted_password = cipher_suite.encrypt(password.encode())
# print(encrypted_password)

decrypted_password = cipher_suite.decrypt('gAAAAABnvZ-K2FU-o72gRBuNKnN23SkNjv_ne88o5cJVt8CbbQFt32U6wnrMqGH7HL8KBfhL8eKnSn3u32-LWm2bEymx0UuxJLD_IDMQo4_Y1vxPnH30eP0=').decode()

print(decrypted_password)
