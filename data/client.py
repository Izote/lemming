from supabase import create_client
from .settings import *

client = create_client(URL, KEY)
