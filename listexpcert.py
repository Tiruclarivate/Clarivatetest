import boto3
acm_client = boto3.client('acm', region_name='us-west-2')
cert_list = acm_client.list_certificates()
# print type( cert_list )
for key in cert_list.keys():
	for x in cert_list[ key ]:
		for y in x.keys():
		 if y == 'CertificateArn':
		 	print( y )	
			print( acm_client.describe_certificate( CertificateArn = x[ 'CertificateArn' ] ) )
