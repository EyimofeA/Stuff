import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# League average offensive ratings (points per 100 possessions)
# Sources: Basketball Reference, FanSided, Sportico
# 2026 playoff value is preliminary (first round in progress as of April 2026)
nba_data = [
    {'season': 2010, 'regular_ortg': 105.3, 'playoff_ortg': 104.6},
    {'season': 2011, 'regular_ortg': 105.2, 'playoff_ortg': 104.8},
    {'season': 2012, 'regular_ortg': 107.5, 'playoff_ortg': 106.3},
    {'season': 2013, 'regular_ortg': 107.1, 'playoff_ortg': 105.9},
    {'season': 2014, 'regular_ortg': 107.6, 'playoff_ortg': 105.8},
    {'season': 2015, 'regular_ortg': 107.8, 'playoff_ortg': 107.1},
    {'season': 2016, 'regular_ortg': 108.6, 'playoff_ortg': 107.9},
    {'season': 2017, 'regular_ortg': 110.0, 'playoff_ortg': 110.8},
    {'season': 2018, 'regular_ortg': 110.9, 'playoff_ortg': 109.2},
    {'season': 2019, 'regular_ortg': 112.1, 'playoff_ortg': 110.9},
    {'season': 2020, 'regular_ortg': 113.7, 'playoff_ortg': 112.8},
    {'season': 2021, 'regular_ortg': 115.0, 'playoff_ortg': 114.2},
    {'season': 2022, 'regular_ortg': 116.4, 'playoff_ortg': 115.9},
    {'season': 2023, 'regular_ortg': 115.9, 'playoff_ortg': 114.8},
    {'season': 2024, 'regular_ortg': 115.3, 'playoff_ortg': 113.0},
    {'season': 2025, 'regular_ortg': 114.5, 'playoff_ortg': 113.0},
    {'season': 2026, 'regular_ortg': 115.7, 'playoff_ortg': 113.5},  # 2026 playoff est.
]

df = pd.DataFrame(nba_data)
df['diff'] = df['regular_ortg'] - df['playoff_ortg']

fig, ax = plt.subplots(figsize=(12, 5))

# Shade above/below zero
ax.fill_between(df['season'], df['diff'], 0,
                where=(df['diff'] >= 0), alpha=0.15, color='steelblue', interpolate=True)
ax.fill_between(df['season'], df['diff'], 0,
                where=(df['diff'] < 0), alpha=0.15, color='tomato', interpolate=True)

ax.plot(df['season'], df['diff'], marker='o', linewidth=2, color='steelblue',
        markerfacecolor='white', markeredgewidth=2, markersize=7)

# Mark the 2026 point as an estimate
ax.plot(2026, df.loc[df['season'] == 2026, 'diff'].values[0],
        marker='o', color='orange', markersize=9, zorder=5,
        label='2026 (playoff est., in progress)')

ax.axhline(0, color='black', linewidth=0.8, linestyle='--')

ax.set_xlabel('Season', fontsize=11)
ax.set_ylabel('Regular Season ORtg − Playoff ORtg\n(pts per 100 poss.)', fontsize=10)
ax.set_title('NBA Offensive Rating Gap: Regular Season vs Playoffs (2010–2026)\n'
             'Positive = Regular season scored more efficiently', fontsize=12, fontweight='bold')

ax.set_xticks(df['season'])
ax.set_xticklabels(df['season'], rotation=45, ha='right')
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax.grid(axis='y', alpha=0.3)
ax.legend(fontsize=9, loc='upper left')

plt.tight_layout()
plt.savefig('/home/user/Stuff/playoff_vs_regular_ratings.png', dpi=150, bbox_inches='tight')
print("Saved: playoff_vs_regular_ratings.png")

print(f"\n{'Season':<8} {'Reg ORtg':<12} {'Playoff ORtg':<14} {'Diff':>6}")
print("-" * 42)
for _, r in df.iterrows():
    flag = " *" if r['season'] == 2026 else ""
    print(f"{int(r['season']):<8} {r['regular_ortg']:<12.1f} {r['playoff_ortg']:<14.1f} {r['diff']:>+.1f}{flag}")
print("\n* 2026 playoff value is preliminary (first round in progress)")
