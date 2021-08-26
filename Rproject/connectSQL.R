install.packages("RODBC")
library(RODBC)

conexao = odbcDriverConnect('driver= {SQL Server};server=gw-dev-db;
                            Database=GW_intDB;User=GW_pcUser;Password=pc%nt%r1;
                            trusted_connection=true')
resultado <- sqlQuery(conexao,"SELECT * FROM dbo.PC_MESSAGE WHERE BOUND = 1")

resultado

odbcClose(conexao)


