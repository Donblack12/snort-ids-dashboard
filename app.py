from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import os
import io
import base64

app = Flask(__name__)

ALERT_FILE = "/var/log/snort/snort.alert.fast"

@app.route("/")
def index():
    if not os.path.exists(ALERT_FILE):
        return "Fichier d'alerte Snort introuvable."

    with open(ALERT_FILE, "r") as f:
        lines = f.readlines()

    alerts = [line.strip() for line in lines if "[**]" in line]

    # Statistiques simples
    alert_counts = {}
    for alert in alerts:
        try:
            msg = alert.split("]")[2].strip()
        except IndexError:
            msg = "Inconnu"
        alert_counts[msg] = alert_counts.get(msg, 0) + 1

    # Génération du graphique
    fig, ax = plt.subplots(figsize=(10, max(3, len(alert_counts) * 0.4)))
    ax.barh(list(alert_counts.keys()), list(alert_counts.values()), color='skyblue')
    ax.set_title("Nombre d'occurrences par alerte")
    ax.set_xlabel("Nombre d'occurrences")
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode()

    return render_template_string("""
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Dashboard Snort</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <meta http-equiv="refresh" content="10">
  </head>
  <body class="bg-light">
    <div class="container mt-4">
      <h1 class="text-center text-primary mb-4">🚨 Dashboard Snort 🚨</h1>

      <div class="card mb-4 shadow-sm">
        <div class="card-body">
          <h4 class="card-title">📊 Graphique des alertes</h4>
          <img src="data:image/png;base64,{{ chart_url }}" class="img-fluid" alt="Graphique des alertes">
        </div>
      </div>

      <div class="card shadow-sm">
        <div class="card-body">
          <h4 class="card-title">🧾 Dernières alertes</h4>
          <table class="table table-bordered table-striped table-sm mt-3">
            <thead class="table-dark">
              <tr>
                <th scope="col">Alerte</th>
              </tr>
            </thead>
            <tbody>
              {% for alert in alerts %}
              <tr>
                <td style="font-size: 0.9rem;">{{ alert }}</td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </body>
</html>
""", alerts=alerts[-20:], chart_url=chart_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
