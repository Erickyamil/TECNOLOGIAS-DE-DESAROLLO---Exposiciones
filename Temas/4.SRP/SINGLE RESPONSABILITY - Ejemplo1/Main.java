public class Main {
    public static void main(String[] args) {
        SistemaPedidos pedidos = new SistemaPedidos("Elias", "Expreso");
        MaquinaCafe cafe = new MaquinaCafe("Espresso");
        Factura factura = new Factura("Elias", 82.50);
        Notificacion notificacion = new Notificacion("Elias", " Tu pedido esta listo");

        pedidos.tomarPedido();
        cafe.prepararCafe();
        factura.generarFactura();
        notificacion.enviarMensaje();

    }
}