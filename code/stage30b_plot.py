#!/usr/bin/env python3
"""Descriptive scientific figure of a proved SPE family, not a proof."""
from pathlib import Path
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from stage30b_within_model_numeric import bilateral,alpha,WI


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--preview',help='Optional local PNG path for visual inspection')
    args=parser.parse_args()
    plt.rcParams.update({'svg.hashsalt':'stage30b','font.size':11})
    fig,ax=plt.subplots(figsize=(8.2,5.0))
    fig.subplots_adjust(left=.12,right=.98,bottom=.24,top=.89)
    K=.55
    for eta,color in [(.10,'#2d6d9d'),(.115,'#d2842f'),(.14,'#237949')]:
        star=alpha(1,eta);aa=np.linspace(0,star,200)
        diffs=[bilateral(1,float(a),eta)['world_noK']-3*WI+K for a in aa]
        ax.plot(aa,diffs,label=fr'$\eta={eta}$',color=color,lw=2.3)
        ax.scatter([star],[diffs[-1]],s=35,color=color,zorder=3)
    ax.axhline(0,color='#424951',lw=1.2,ls='--',label='Every broad-agenda public SPE')
    ax.set(xlabel='Commonality stock a (common compatibility stock c = 1)',
           ylabel='Private minus public world welfare',xlim=(-.01,.62),
           ylim=(-.12,.095),title='Private equilibria can lie on both sides of public welfare')
    ax.grid(axis='y',alpha=.2);ax.spines[['top','right']].set_visible(False)
    ax.legend(frameon=False,loc='upper left',fontsize=9)
    fig.text(.5,.035,'K = .55. Solid curves: supported private SPE under exclusive outsider agenda or unanimity.\n'
             'Endpoints: privately optimal designs. This plot shows the c = 1 slice; the full set also includes c < 1.',
             ha='center',fontsize=9)
    path=Path('docs/audit/STAGE30B_EQUILIBRIUM_WELFARE.svg')
    fig.savefig(path,bbox_inches='tight',metadata={'Date':None})
    if args.preview:fig.savefig(args.preview,dpi=150,bbox_inches='tight')
    plt.close(fig)


if __name__=='__main__':main()
