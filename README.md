# Why These Clones Exist

UserStyles.world (USw) (https://userstyles.world/) repository restricts each UserStyle to a single domain slug ("Category"), which prevents native multi-site support for independent domains sharing the same layout.


## The Limitations of USw

* **Single-Slug Restriction:** A style can only target one category/slug. While this works for unified brands with matching TLD variations (e.g., `bbc.com` and `bbc.co.uk`), it fails for separate domains with entirely different names (e.g., `rferl.org` and `currenttime.tv`).
* **No Multi-Domain Targeting:** USw provides no mechanism to associate a single repository entry with multiple distinct domain names.
* **Duplicate `@name` Restriction:** USw rejects multiple styles if they share an identical `@name` metadata property.

## Why Clones Are Necessary

Manually updating separate, independent entries on USw for every minor code change is impractical. These clones serve as a workaround to deploy identical styles across distinct domains despite USw's platform restrictions.


# How This Branch Works

To maintain a single source of truth across multiple USw entries, this repository uses an automated build and deployment pipeline via GitHub Actions.

## Daily Synchronization Pipeline

1. **Development & Initial Upload:**
The base UserStyle is edited using the Stylus browser extension editor and published to UserStyles.world (USw).
2. **Automated Modification & Cloning:**
Once a day, a GitHub Action fetches the latest version of the primary UserStyle from USw and compares it against the previously saved commit. If changes are detected, the workflow automatically generates domain-specific clones in the `site-clones` branch, assigning a unique `@name` property to each clone.
3. **Automated USw Updates:**
Each cloned entry on USw is linked back to its corresponding clone file in this GitHub repository. USw periodically syncs with GitHub to fetch the updated styles (checking every 4 hours at minute 4).

> **Note on Timing:** Since USw checks for updates every 4 hours, all cloned entries propagate to USw shortly after the daily GitHub Action runs past midnight UTC.
