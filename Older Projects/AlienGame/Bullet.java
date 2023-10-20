import java.awt.*;
import java.util.*;
import javax.swing.*;
public class Bullet extends Creature
{
   private int speed;
   private double direction;
   private double vx;
   private double vy;
   public Bullet(int x, int y, int s, double a, String imageName,int mx,int my)
   {
      super(imageName);
      isVisible=true;
      speed=s;
      myX=x;
      myY=y;
      direction=a;
      vx=(myX-mx)/-100;
      vy=(myY-my)/-100;
   }
   public void detect()
   {
      if(myX<1||myX>Map.SIDE)
      {
         isVisible=false;
      }
      if(myY<1||myY>Map.BOTTOM)
      {
         isVisible=false;
      }
   }
   public void move()
   {
      double radians=direction*Math.PI/180.0;
      double dx=(speed*Math.cos(radians));
      double dy=(speed*Math.sin(radians));
      myX=(int)(myX+dx);
      myY=(int)(myY+dy);
      
     // myY=(int)(myY+vy);
     // myX=(int)(myX+vx);
      
   }
   
   
}
      
   