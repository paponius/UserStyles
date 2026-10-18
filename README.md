> **Note**: It seems that when a UserCSS on USw is "Mirrored", these limits do not apply.
> There is no problem with duplicate @name. (Also the length limit for name and description is ignored.)
> That makes this branch and workflow useless. I started to use links directly to main branch for cloned UserCSS.
> Some are still using links to this branch.

# ⚠️ Automated Branch Notice

> **Note:** The `site-clones` branch is automatically managed and updated daily by GitHub Actions.

- **Generated Content:** The root userstyle files on this branch are generated automatically from primary output templates.
- **File Deletions:** Any files deleted or renamed in the style generation process are purged from this branch on every workflow run to prevent stale assets.
- **Manual Edits:** Direct modifications or manual file additions made to this branch will be overwritten or removed during the next automated run.


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
