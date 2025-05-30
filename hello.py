from preswald import connect, get_df
from preswald import query
from preswald import table, text
from preswald import plotly
import plotly.express as px

connect()
df = get_df("ai_csv")

sql = "SELECT hours_coding, sleep_hours, cognitive_load FROM ai_csv WHERE CAST(hours_coding AS FLOAT) > 4"
filtered_df = query(sql, "ai_csv")

text("# AI Dev Productivity Analysis App")
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x="column1", y="column2", color="category")
plotly(fig)
