# === Stage 16: Add argparse support for the most common commands ===
# Project: PantryMate
import argparse, json, sys

def parse_args():
    p = argparse.ArgumentParser(description='PantryMate CLI')
    sub = p.add_subparsers(dest='cmd', help='Available commands')

    # list items
    ls = sub.add_parser('list', help='List pantry items')
    ls.add_argument('--sort', choices=['name','expiry'], default='name')
    ls.add_argument('-n', '--count', type=int, help='Show only first N items')

    # add item
    ad = sub.add_parser('add', help='Add a new item')
    ad.add_argument('name', help='Item name')
    ad.add_argument('--qty', '-q', type=float, default=1.0)
    ad.add_argument('--exp', '--expiry-date', help='YYYY-MM-DD expiry date')

    # remove item
    rm = sub.add_parser('remove', help='Remove an item by index')
    rm.add_argument('idx', type=int, help='Index of item to remove')

    # usage log
    ul = sub.add_parser('use', help='Log usage of an item')
    ul.add_argument('--item', required=True, help='Item name')
    ul.add_argument('--qty', '-q', type=float, default=1.0)

    # restock alert
    ra = sub.add_parser('restock', help='Show items needing restock')
    ra.add_argument('--min-qty', '-m', type=float, default=0.5)
    ra.add_argument('--days', '-d', type=int, help='Alert only if expiry within N days')

    # shopping list (synonym for list with sort=expiry)
    sl = sub.add_parser('shopping-list', aliases=['sl'], help='Show items expiring soon')
    sl.add_argument('--sort', choices=['name','expiry'], default='expiry')

    return p.parse_args()
