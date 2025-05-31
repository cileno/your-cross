import psycopg2 as psycopg
try:
    conn = psycopg.connect(
        dbname="yourcrossdb",
        user="admin",
        password="@dm1n15trAd0r",
        host="localhost",
        port="5432"
    )
    print("✅ Conexão com o banco de dados bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"❌ Erro na conexão: {e}")