  import javax.swing.*;

public class Driver
{
   
   public static void main(String[] args)
   {
      JFrame frame=new JFrame("game");
      frame.setSize(800,700);
      frame.setLocation(0,0);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new Map());
      frame.setVisible(true);
   }
   
      
}