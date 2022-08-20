import kivy.app
import kivy.uix.screenmanager
import kivy.config


class ScreenManagement(kivy.uix.screenmanager.ScreenManager):
    pass


class IntroScreen(kivy.uix.screenmanager.Screen):
    pass


class GamesScreen(kivy.uix.screenmanager.Screen):
    pass


class GamesLauncherApp(kivy.app.App):
    pass


if __name__ == '__main__':
    app = GamesLauncherApp()

    app.title = 'Games Launcher'
    kivy.config.Config.set('graphics', 'resizable', '0')
    kivy.config.Config.set('graphics', 'width', '1000')
    kivy.config.Config.set('graphics', 'height', '700')

    app.run()