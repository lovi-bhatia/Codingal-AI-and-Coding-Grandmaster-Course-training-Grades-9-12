import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try: df = pd.read_csv("AI_EXPERT_HANDS_ON/Module_1/imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The primary dataset 'imdb_top_1000.csv' is missing from the local environment."); raise SystemExit

genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p): return "Positive State 😊" if p > 0 else "Negative State 😞" if p < 0 else "Neutral State 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    d = df
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty: return "No matching data points found in the current parameter space."
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == n: break
    return out if out else "No matching data points found in the current parameter space."

def show(recs, name):
    print(Fore.YELLOW + f"\n🍿 Algorithmically Curated Stimuli for Observer {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. 🎥 {t} (Valence Metric: {p:.2f}, {senti(p)})")

def get_genre():
    print(Fore.GREEN + "Available Narrative Categories: ", end="")
    for i, g in enumerate(genres, 1): print(f"{Fore.CYAN}{i}. {g}")
    print()
    while True:
        x = input(Fore.YELLOW + "Input category index or label: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(genres): return genres[int(x) - 1]
        x = x.title()
        if x in genres: return x
        print(Fore.RED + "Unrecognized input state. Please recalibrate and try again.\n")

def get_rating():
    while True:
        x = input(Fore.YELLOW + "Set minimum quality threshold (7.6-9.3) or type 'skip': ").strip()
        if x.lower() == "skip": return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3: return r
            print(Fore.RED + "Threshold exceeds defined bounds. Please adjust.\n")
        except ValueError:
            print(Fore.RED + "Unrecognized input state. Please recalibrate and try again.\n")

print(Fore.BLUE + "🌌 Welcome to the Cognitive-Quantum Stimuli Recommender! 🌌\n")
name = input(Fore.YELLOW + "What is your observer designation? ").strip()
print(f"\n{Fore.GREEN}Neural link established, {name}!\n")
print(Fore.BLUE + "\n🔬 Let us optimize the media parameters for your current cognitive state!\n")

genre = get_genre()
mood = input(Fore.YELLOW + "Describe your current emotional valence: ").strip()
print(Fore.BLUE + "\nProcessing cognitive state", end="", flush=True); dots()
mp = TextBlob(mood).sentiment.polarity
md = "positive 😊" if mp > 0 else "negative 😞" if mp < 0 else "neutral 😐"
print(f"\n{Fore.GREEN}Your cognitive baseline is {md} (Valence Metric: {mp:.2f}).\n")

rating = get_rating()
print(f"{Fore.BLUE}\nCollapsing probability wave to find optimal stimuli for {name}", end="", flush=True); dots()
recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)

while True:
    a = input(Fore.YELLOW + "\nShall we run another sampling iteration? (yes/no): ").strip().lower()
    if a == "no":
        print(Fore.GREEN + f"\nMay these stimuli enrich your neural pathways, {name}! 🧠🌌\n"); break
    if a == "yes":
        recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
        print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print(Fore.RED + "Input unrecognized. Please provide a binary response.\n")