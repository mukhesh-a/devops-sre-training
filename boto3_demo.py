"""
Python Boto3 Package Demo - For DevOps Interns
==============================================
AWS SDK: create clients, call APIs. Uses default credentials (no tokens in code).
Configure via: AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY, or ~/.aws/credentials,
or IAM role (EC2/ECS/Lambda).

Install: pip install boto3   (or: python -m pip install boto3)
"""

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

print("=" * 60)
print("BOTO3 PACKAGE - AWS CLIENTS (Default Credentials)")
print("=" * 60)

# =============================================================================
# 1. CREATING A CLIENT (NO TOKENS IN CODE)
# =============================================================================
print("\n--- 1. CREATING A CLIENT ---")
print("Credentials come from env vars, ~/.aws/credentials, or IAM role.")

# Default: uses default profile / env vars
sts_client = boto3.client("sts")
print("  sts_client = boto3.client('sts')")

# Optional: specify region
s3_client = boto3.client("s3", region_name="us-east-1")
print("  s3_client = boto3.client('s3', region_name='us-east-1')")

# Optional: use a named profile (e.g. from ~/.aws/credentials)
# session = boto3.Session(profile_name='my-profile')
# s3 = session.client('s3')

# =============================================================================
# 2. CHECK IDENTITY (STS - WHO AM I?)
# =============================================================================
print("\n--- 2. STS GET_CALLER_IDENTITY (who am I?) ---")


def get_caller_identity():
    """No explicit token; uses default credentials. Returns account/user/arn or None."""
    try:
        response = sts_client.get_caller_identity()
        return response
    except NoCredentialsError:
        print("  NoCredentialsError: Set AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY or run 'aws configure'")
        return None
    except ClientError as e:
        print(f"  ClientError: {e}")
        return None


identity = get_caller_identity()
if identity:
    print(f"  Account: {identity.get('Account')}")
    print(f"  Arn:     {identity.get('Arn')}")
    print(f"  UserId:  {identity.get('UserId')}")
else:
    print("  (Skipping AWS calls - no credentials. Code pattern shown above.)")

# =============================================================================
# 3. S3 - LIST BUCKETS (READ-ONLY, SAFE DEMO)
# =============================================================================
print("\n--- 3. S3 LIST BUCKETS ---")


def list_s3_buckets():
    """List bucket names; no explicit auth; uses default credentials."""
    try:
        response = s3_client.list_buckets()
        names = [b["Name"] for b in response.get("Buckets", [])]
        return names
    except NoCredentialsError:
        print("  NoCredentialsError: configure AWS credentials")
        return []
    except ClientError as e:
        print(f"  ClientError: {e}")
        return []


buckets = list_s3_buckets()
if buckets:
    print(f"  Buckets ({len(buckets)}): {buckets[:5]}{'...' if len(buckets) > 5 else ''}")
else:
    print("  No buckets or credentials not configured.")

# =============================================================================
# 4. EC2 - DESCRIBE INSTANCES (READ-ONLY)
# =============================================================================
print("\n--- 4. EC2 DESCRIBE INSTANCES (read-only) ---")

ec2_client = boto3.client("ec2", region_name="us-east-1")


def list_ec2_instances(region_name="us-east-1"):
    """Describe instances in a region; uses default credentials."""
    try:
        ec2 = boto3.client("ec2", region_name=region_name)
        response = ec2.describe_instances()
        instance_ids = []
        for reservation in response.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instance_ids.append(instance.get("InstanceId"))
        return instance_ids
    except NoCredentialsError:
        print("  NoCredentialsError: configure AWS credentials")
        return []
    except ClientError as e:
        print(f"  ClientError: {e}")
        return []


instances = list_ec2_instances()
if instances:
    print(f"  Instances: {instances[:5]}{'...' if len(instances) > 5 else ''}")
else:
    print("  No instances in region or credentials not configured.")

# =============================================================================
# 5. RESPONSE STRUCTURE - METADATA AND RESULT
# =============================================================================
print("\n--- 5. RESPONSE STRUCTURE ---")
print("  AWS API responses are dicts with keys like 'ResponseMetadata', plus service-specific keys.")

if identity:
    print(f"  identity keys: {list(identity.keys())}")
    print("  ResponseMetadata contains HTTPStatusCode, RequestId, etc.")

# =============================================================================
# 6. ERROR HANDLING PATTERN
# =============================================================================
print("\n--- 6. ERROR HANDLING (ClientError, NoCredentialsError) ---")


def safe_describe_regions():
    """Describe regions; show try/except pattern."""
    try:
        ec2 = boto3.client("ec2")
        response = ec2.describe_regions()
        return [r["RegionName"] for r in response.get("Regions", [])]
    except NoCredentialsError:
        print("  NoCredentialsError: no credentials in env or config")
        return []
    except ClientError as e:
        code = e.response.get("Error", {}).get("Code", "")
        print(f"  ClientError: {code}")
        return []


regions = safe_describe_regions()
if regions:
    print(f"  Regions (sample): {regions[:3]}...")
else:
    print("  (No regions listed - credentials may be missing)")

# =============================================================================
# QUICK REFERENCE
# =============================================================================
print("\n" + "=" * 60)
print("QUICK REFERENCE")
print("=" * 60)
print("""
  boto3.client('service')           -> create client (default creds)
  boto3.client('s3', region_name='us-east-1')  -> with region
  response = client.method(**kwargs) -> call API; response is a dict
  NoCredentialsError               -> no env / profile / role
  ClientError                       -> API error (check response['Error']['Code'])

  No tokens in code: use AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, or
  ~/.aws/credentials, or IAM role for EC2/ECS/Lambda.
""")
print("Done.")
