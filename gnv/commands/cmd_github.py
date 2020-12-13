import click
from selenium import webdriver
from time import sleep


def create_repo(name, un, pd, option, readme, des):
    browser = webdriver.Chrome()
    browser.get("https://www.github.com")
    sleep(3)
    sign_btn = browser.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
    sign_btn.click()
    sleep(3)
    username = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]")
    username.clear()
    username.send_keys(un)
    sleep(2)
    password = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]")
    password.clear()
    password.send_keys(pd)
    sleep(2)
    login_btn = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]")
    login_btn.click()
    sleep(3)
    new_repo_btn = browser.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a")
    new_repo_btn.click()
    sleep(2)
    repo_name = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input")
    repo_name.clear()
    repo_name.send_keys(name)
    sleep(2)
    description = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/dl/dd/input")
    description.clear()
    description.send_keys(des)
    sleep(2)
    if option == "pub":
        public_repo = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/div[1]/label")
        public_repo.click()
        sleep(2)
    elif option == "pri":
        private_repo = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/div[2]/label")
        private_repo.click()
        sleep(2)
    else:
        public_repo = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/div[1]/label")
        public_repo.click()
        click.echo(f"Bad command {option}, the repo is taken to be public")
    if readme == "y":
        read_me = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label")
        read_me.click()
        sleep(2)
    elif readme == "n":
        click.echo("Didn't add a Read me file to your repo as told by you")
        sleep(2)
    else:
        click.echo(f"Bad command {readme}, could not add a readme file")
        sleep(2)
    done = browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button")
    done.click()
    sleep(3)
    dropdownicon = browser.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/span[2]")
    dropdownicon.click()
    sleep(2)
    signout = browser.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button")
    signout.click()
    sleep(3)
    browser.close()
    click.echo(f"Successfully created {name} at https://github.com/{un}/{name}")
    click.echo(" -------------------------------------------------------------------------------------------------------------------")
    click.echo(f"| Run the following commands in your project directory to upload files to your repo                                ")
    click.echo(f"| git add <file-name> or git add .                                                                                 ")
    click.echo(f'| git commit -m "commit text"                                                                                      ')
    click.echo(f"| git branch -M <branch-name>                                                                                      ")
    click.echo(f"| git remote add origin https://github.com/{un}/{name}.git                                                         ")
    click.echo(f"| git push -u origin <branch-name>                                                                                 ")
    click.echo(f"| If you want to clone the repo then type git clone https://github.com/{un}/{name}.git in your desired directory   ")
    click.echo(" -------------------------------------------------------------------------------------------------------------------")


def delete_repo(name, un, pd, confirm):
    if confirm == "y":
        browser = webdriver.Chrome()
        browser.get("https://www.github.com")
        sleep(3)
        sign_btn = browser.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
        sign_btn.click()
        sleep(3)
        username = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]")
        username.clear()
        username.send_keys(un)
        sleep(2)
        password = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]")
        password.clear()
        password.send_keys(pd)
        sleep(2)
        login_btn = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]")
        login_btn.click()
        sleep(3)
        browser.get(f"https://github.com/{un}/{name}")
        sleep(3)
        browser.get(f"https://github.com/{un}/{name}/settings")
        sleep(3)
        delete_btn = browser.find_element_by_css_selector("#options_bucket > div.Box.Box--danger > ul > li:nth-child(4) > details > summary")
        delete_btn.click()
        sleep(3)
        delete_text = browser.find_element_by_css_selector("#options_bucket > div.Box.Box--danger > ul > li:nth-child(4) > details > details-dialog > div.Box-body.overflow-auto > form > p > input")
        delete_text.clear()
        delete_text.send_keys(f"{un}/{name}")
        sleep(2)
        confirmed = browser.find_element_by_css_selector("#options_bucket > div.Box.Box--danger > ul > li:nth-child(4) > details > details-dialog > div.Box-body.overflow-auto > form > button")
        confirmed.click()
        sleep(3)
        dropdownicon = browser.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/span[2]")
        dropdownicon.click()
        sleep(2)
        signout = browser.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button")
        signout.click()
        sleep(3)
        browser.close()
        click.echo(f"Successfully deleted {name} at https://github.com/{un}/{name}")
    elif confirm == "n":
        click.echo(f"Aborted the deletion of {name} repo")
    else:
        click.echo(f"Failed to delete {name} repo")


@click.group()
def cli():
    pass


@click.command(help="Creates Repo to Github")
@click.argument("name", type=str)
@click.option('-u', "--un", required=True, prompt="username or e-mail", help="GitHub username or email")
@click.option('-p', "--pd", required=True, hide_input=True, prompt="password", help="Github Password")
@click.option('-d', "--des", prompt="A sweet description of your repo", help="Adds Description to the repo")
@click.option('-s', "--private", prompt="The repo is private or public[pri/pub]", help="Repo is Private or Public")
@click.option('-r', "--readme", prompt="Do you add a Readme file to your repo[y/n]", help="Addition of a readme file to the repo")
@click.pass_context
def create(ctx, name, un, pd, des, private, readme):
    """
    Creates GitHub Repositories
    """
    ctx.invoke(create_repo, name=name, un=un, pd=pd, des=des, option=private, readme=readme)


@click.command(help="Deletes the Repo from Github")
@click.argument("name", type=str)
@click.option('-u', "--un", required=True, prompt="username or e-mail", help="GitHub username or email")
@click.option('-p', "--pd", required=True, hide_input=True, prompt="password", help="Github Password")
@click.option('-c', "--confirm", prompt="Are you sure that you want to delete this repo[y/n]", help="Confirmation to delete the repo")
@click.pass_context
def delete(ctx, name, un, pd, confirm):
    """
    Deletes GitHub Repositories
    """
    ctx.invoke(delete_repo, name=name, un=un, pd=pd, confirm=confirm)


cli.add_command(create)
cli.add_command(delete)
