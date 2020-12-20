import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def create_repo(name, un, pd, option, readme, des):
    browser = webdriver.Chrome()
    browser.get("https://www.github.com/login")
    sleep(3)
    try:
        username = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "login_field")))
        username.clear()
        username.send_keys(un)
        passwd = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "password")))
        passwd.clear()
        passwd.send_keys(pd)
        login_btn = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.NAME, "commit")))
        login_btn.click()
        browser.get("https://www.github.com/new")
        repo_name = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "repository_name")))
        repo_name.clear()
        repo_name.send_keys(name)
        description = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "repository_description")))
        description.clear()
        description.send_keys(des)
        if option == "pub":
            pub_tog = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "repository_visibility_public")))
            pub_tog.click()
        elif option == "pri":
            pri_tog = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "repository_visibility_private")))
            pri_tog.click()
            sleep(2)
        else:
            pub_tog = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "repository_visibility_public")))
            pub_tog.click()
            click.echo(f"Bad command {option}, the repo is taken to be public")
        if readme == "y":
            read_me = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "repository_auto_init")))
            read_me.click()
            sleep(2)
        elif readme == "n":
            click.echo("Didn't add a Read me file to your repo as you told")
            sleep(2)
        else:
            click.echo(f"Bad command {readme}, could not add a readme file")
            sleep(2)
            done_btn = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#new_repository > div.js-with-permission-fields > button")))
            done_btn.click()
            drop_down = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
            drop_down.click()
            sleep(2)
            sign_out = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
            sign_out.click()
            sleep(2)
    except:
        browser.quit()
    click.echo(f"Successfully created {name} at https://github.com/{un}/{name}")
    click.echo(f"Run the following commands in your project directory to upload files to your repo:")
    click.echo(f"git add <file-name> or git add .")
    click.echo(f'git commit -m "commit text"')
    click.echo(f"git branch -M <branch-name>")
    click.echo(f"git remote add origin https://github.com/{un}/{name}.git")
    click.echo(f"git push -u origin <branch-name>")
    click.echo(f"If you want to clone the repo then type git clone https://github.com/{un}/{name}.git in your desired directory")


def delete_repo(name, un, pd, confirm):
    if confirm == "y":
        browser = webdriver.Chrome()
        browser.get("https://www.github.com/login")
        sleep(2)
        try:
            username = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "login_field")))
            username.clear()
            username.send_keys(un)
            passwd = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "password")))
            passwd.clear()
            passwd.send_keys(pd)
            login_btn = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.NAME, "commit")))
            login_btn.click()
            browser.get(f"https://www.github.com/{un}/{name}/settings")
            delete = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')))
            delete.click()
            delete_name = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')))
            delete_name.clear()
            delete_name.send_keys(f"{un}/{name}")
            confirm_btn = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')))
            confirm_btn.click()
            drop_down = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
            drop_down.click()
            sleep(2)
            sign_out = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button')))
            sign_out.click()
            sleep(2)
        except:
            browser.quit()
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
@click.option('-u', "--un", required=True, prompt="username", help="GitHub username")
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
@click.option('-u', "--un", required=True, prompt="username", help="GitHub username")
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
