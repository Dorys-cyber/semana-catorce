from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def main():
    # Instancia del servicio compartido
    servicio = RestauranteServicio()

    def abrir_menu_principal(usuario_autenticado):
        app_main = MainView(usuario_autenticado, servicio)
        app_main.mainloop()

    # Iniciar ventana de Login
    login_app = LoginView(servicio, on_login_success=abrir_menu_principal)
    login_app.mainloop()

if __name__ == "__main__":
    main()