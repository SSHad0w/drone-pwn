![2b144cde7adf12a9c2998a33a336c7ff.png](../../_resources/2b144cde7adf12a9c2998a33a336c7ff.png)

`git init`

`git add py_print_parser_test.py`

`git commit -m "Updating the parser with new features."`

`git branch -M main`

`git remote add origin https://github.com/SSHAD0w/drone-pwn/`

`git push https://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@github.com/SSHAD0w/drone-pwn.git`

![a60cc8ba0bfc0660f40d61b0421cf3f9.png](../../_resources/a60cc8ba0bfc0660f40d61b0421cf3f9.png)

`git pull https://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@github.com/SSHAD0w/drone-pwn.git`


![e3a986f7ad7d6c8ab897487c30bf1c3d.png](../../_resources/e3a986f7ad7d6c8ab897487c30bf1c3d.png)

`git remote add origin2 https://github.com/SSHAD0w/drone-pwn/`

`git pull origin2 main` 

[Doesn't work]

` git pull https://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@github.com/SSHAD0w/drone-pwn.git main`

Throws an error:

```
From https://github.com/SSHAD0w/drone-pwn
 * branch            main       -> FETCH_HEAD
fatal: refusing to merge unrelated histories
```

[This should help.](https://www.educative.io/edpresso/the-fatal-refusing-to-merge-unrelated-histories-git-error)

`git pull https://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@github.com/SSHAD0w/drone-pwn.git main --allow-unrelated-histories`

```
From https://github.com/SSHAD0w/drone-pwn
 * branch            main       -> FETCH_HEAD
error: Your local changes to the following files would be overwritten by merge:
  custom_file_name.txt
```

Seems like it worked.

Now that the pull is finished. I can push. (Hopefully.)

`git remote add origin3 https://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@github.com/SSHAD0w/drone-pwn.git
`


```
$ git push origin3 main
To https://github.com/SSHAD0w/drone-pwn.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/SSHAD0w/drone-pwn.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

![05df219910a90536e42d68f6beb8e8d8.png](../../_resources/05df219910a90536e42d68f6beb8e8d8.png)

[So I looked up how to add to git](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

[When that errored out, I found that I had to use the -f flag](https://stackoverflow.com/questions/39399804/updates-were-rejected-because-the-tip-of-your-current-branch-is-behind-its-remot/39400690#39400690)


I am a little offput because the last time I did this, I got rid of a lot of work on accident. I will make a backup before doing it this time. 

`git push origin3 main -f`

```
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 870 bytes | 870.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/SSHAD0w/drone-pwn.git
 + 11abcdc...9ebff97 main -> main (forced update)
```

It uploaded!

![4e0307c46611909874618e08ebc163e2.png](../../_resources/4e0307c46611909874618e08ebc163e2.png)

Seems like it successfully uploaded... but deleted everything else. Just as I hypothisised. 

I'm glad I made backups.

# Now I know that I should never use the -f flag.


Just as I created a backup with `git pull https://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@github.com/SSHAD0w/drone-pwn.git main` on a different machine, I will restore the backup using 